from django.apps import apps
from django.test import TransactionTestCase
from django.db.migrations.executor import MigrationExecutor
from django.db import connection


class MigrationTestCase(TransactionTestCase):
    # https://www.caktusgroup.com/blog/2016/02/02/writing-unit-tests-django-migrations/

    @property
    def app(self):
        return apps.get_containing_app_config(type(self).__module__).name

    migrate_from = None
    migrate_to = None

    def setUp(self):
        assert self.migrate_from and self.migrate_to, \
            ("TestCase '{}' must define migrate_from and "
             "migrate_to properties".format(type(self).__name__))
        self.migrate_from = [(self.app, self.migrate_from)]
        self.migrate_to = [(self.app, self.migrate_to)]
        executor = MigrationExecutor(connection)
        old_apps = executor.loader.project_state(self.migrate_from).apps

        # Reverse to the original migration
        executor.migrate(self.migrate_from)

        self.setUpBeforeMigration(old_apps)

        # This wasn't part of the original code from the blog post, but
        # was mentioned as a required workaround in the comments.
        executor = MigrationExecutor(connection)

        # Run the migration to test
        executor.migrate(self.migrate_to)

        self.apps = executor.loader.project_state(self.migrate_to).apps

    def setUpBeforeMigration(self, apps):
        pass


class TestPopulateIsBillable(MigrationTestCase):
    migrate_from = '0012_add_is_billable'
    migrate_to = '0013_populate_is_billable'

    BILLABLE = 0
    NON_BILLABLE = 1

    def setUpBeforeMigration(self, apps):
        Project = apps.get_model('projects', 'Project')
        self.billable_id = Project.objects.create(
            billable=self.BILLABLE
        ).id
        self.non_billable_id = Project.objects.create(
            billable=self.NON_BILLABLE
        ).id

    def test_migration_works(self):
        Project = self.apps.get_model('projects', 'Project')

        self.assertTrue(
            Project.objects.get(id=self.billable_id).is_billable
        )

        self.assertFalse(
            Project.objects.get(id=self.non_billable_id).is_billable,
        )
