from django.test import TestCase

from projects.models import Project


class ApiTests(TestCase):
    def test_api_root_is_ok(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_projects_is_ok(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)

    def test_projects_pk_is_ok(self):
        project = Project(name='Boop')
        project.save()

        response = self.client.get('/api/projects/%d/' % project.id)
        self.assertEqual(response.status_code, 200)

        json = response.json()

        self.assertEqual(json['name'], 'Boop')
