import csv
import logging

from django.core.management.base import BaseCommand
from django.db import transaction

from projects.models import Project


logger = logging.getLogger(__name__)


class DryRunFinished(Exception):
    pass


class Command(BaseCommand):
    help = 'Import projects from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            help='CSV file to import.'
        )
        parser.add_argument(
            '--dry-run',
            default=False,
            help='Don\'t commit imported data to database.',
            action='store_true'
        )

    def import_project(self, row, row_num):
        logger.info("Importing row {}...".format(row_num))

        name = row['full name']
        if not name:
            logger.warn("Skipping! (no name)")
            return

        slug = row['name'] or name.replace(' ', '-').lower()
        tock_id = int(row['Tock ID']) if row['Tock ID'] else None

        p = Project(
            name=name,
            slug=slug,
            tock_id=tock_id,
            tagline=row['tagline'],
            description=row['description'],
            impact=row['impact'],
            github_url=row['github'],
            live_site_url=row['link to live site'],
        )
        p.save()

    def import_csv(self, filename):
        with open(filename, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Skip first row
            next(reader)

            for i, row in enumerate(reader):
                self.import_project(row, i + 1)

    def handle(self, **options):
        try:
            with transaction.atomic():
                self.import_csv(options['filename'])
                if options['dry_run']:
                    raise DryRunFinished()
        except DryRunFinished:
            logger.info('Dry run complete.')
