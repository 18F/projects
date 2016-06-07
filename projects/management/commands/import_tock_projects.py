import textwrap
import logging
import json
from argparse import RawTextHelpFormatter
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify

from projects.models import Project


logger = logging.getLogger(__name__)


class DryRunFinished(Exception):
    pass


class Command(BaseCommand):
    help = textwrap.dedent("""
    Imports projects exported from the Tock API.

    To export projects from the Tock API, save the following URL
    while logged-in to Tock from your browser:

        https://tock.18f.gov/api/projects.json?page_size=1000
    """)

    def create_parser(self, *args, **kwargs):
        # http://stackoverflow.com/a/35470682
        parser = super(Command, self).create_parser(*args, **kwargs)
        parser.formatter_class = RawTextHelpFormatter
        return parser

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            help='Path to JSON export from Tock API'
        )
        parser.add_argument(
            '--dry-run',
            default=False,
            help='Don\'t commit imported data to database.',
            action='store_true'
        )

    def load(self, filename):
        with open(filename) as f:
            content = json.load(f)
            assert content['next'] is None and content['previous'] is None
            results = content['results']
            for result in results:
                tock_id = result['id']
                name = result['name']
                if result['billable']:
                    billable = Project.BILLABLE
                else:
                    billable = Project.NON_BILLABLE
                logname = '%s (#%d)' % (name, tock_id)

                if Project.objects.filter(tock_id=tock_id).exists():
                    logger.info('%s exists.' % logname)
                    continue

                print("Creating entry for %s." % logname)
                project = Project(
                    name=name,
                    slug=slugify(name),
                    billable=billable,
                    tock_id=tock_id
                )
                project.save()

    def handle(self, **options):
        try:
            with transaction.atomic():
                self.load(options['filename'])
                if options['dry_run']:
                    raise DryRunFinished()
        except DryRunFinished:
            logger.info('Dry run complete.')
