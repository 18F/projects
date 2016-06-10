from django.test import TestCase

from ..forms import ProjectForm


class ProjectFormTestCase(TestCase):
    def test_form_contains_autocomplete_url(self):
        self.assertTrue('/client-autocomplete/' in ProjectForm().as_p())
