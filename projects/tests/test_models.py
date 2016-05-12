from django.test import TestCase
from django.db.utils import IntegrityError

from ..models import Project


class ProjectTests(TestCase):
    def test_tock_ids_are_unique(self):
        Project(tock_id=1).save()

        with self.assertRaises(IntegrityError):
            Project(tock_id=1).save()

    def test_many_tock_ids_can_be_null(self):
        Project(tock_id=None).save()
        Project(tock_id=None).save()
