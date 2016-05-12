import csv
from django.db import transaction
from django.core.management.base import BaseCommand

from ...models import Project

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

    def unicode_row(self, row):
        return [item.decode('utf-8') for item in row]

    def import_project(self, row, row_num):
        slug = row['name']

        self.stdout.write("Importing row %d (%s)...\n" % (row_num, slug))

        if row['Tock ID']:
            tock_id = int(row['Tock ID'])
        else:
            tock_id = None

        p = Project(
            name=row['full name'],
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
            row_num = 2
            for row in reader:
                if row_num > 2:
                    # Skip this row, it's just helpful info about the
                    # first row.
                    self.import_project(row, row_num)
                row_num += 1

    def handle(self, **options):
        try:
            with transaction.atomic():
                self.import_csv(options['filename'])
                if options['dry_run']:
                    raise DryRunFinished()
        except DryRunFinished:
            self.stdout.write('Dry run complete.')
