import boto3
import csv
import logging

from tempfile import NamedTemporaryFile

from django.conf import settings
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
        parser.add_argument(
            '--use-s3',
            default=False,
            action='store_true',
            help='Is file in our S3 bucket?',
        )

    def add_project(self, row, row_num):
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

    def parse_file(self, filename):
        with open(filename, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Skip first row
            next(reader)

            for i, row in enumerate(reader):
                self.add_project(row, i + 1)

    def import_s3(self, filename):
        s3 = boto3.resource(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        with NamedTemporaryFile() as f:
            s3.meta.client.download_file(settings.AWS_BUCKET, filename, f.name)
            return self.parse_file(f.name)

    def load(self, filename, use_s3):
        if use_s3:
            return self.import_s3(filename)

        return self.parse_file(filename)

    def handle(self, **options):
        try:
            with transaction.atomic():
                self.load(options['filename'], options['use_s3'])
                if options['dry_run']:
                    raise DryRunFinished()
        except DryRunFinished:
            logger.info('Dry run complete.')
