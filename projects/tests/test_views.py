from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Client


class ClientAutocompleteTestCase(TestCase):
    def setUp(self):
        Client(
            department='Judicial Branch',
            agency='Supreme Court of the United States'
        ).save()
        super().setUp()

    def assertResultsAreEmpty(self, q):
        self.assertEqual(self.get_results(q), {
            'pagination': {'more': False},
            'results': []
        })

    def assertResultsAreNotEmpty(self, q):
        self.assertEqual(
            self.get_results(q)['results'][0]['text'],
            'Judicial Branch - Supreme Court of the United States'
        )

    def get_results(self, q='supreme'):
        res = self.client.get('/client-autocomplete/?q=' + q)
        self.assertEqual(res.status_code, 200)
        return res.json()

    def login_as_staff(self):
        user = User.objects.create_user('foo')
        user.is_staff = True
        user.save()
        self.client.force_login(user)

    def test_results_are_empty_when_unauthenticated(self):
        self.assertResultsAreEmpty('supreme')

    def test_results_are_empty_when_not_staff(self):
        user = User.objects.create_user('foo')
        self.client.force_login(user)
        self.assertResultsAreEmpty('supreme')

    def test_results_are_empty_when_query_has_no_matches(self):
        self.login_as_staff()
        self.assertResultsAreEmpty('blarg')

    def test_results_are_nonempty_when_query_matches_agency(self):
        self.login_as_staff()
        self.assertResultsAreNotEmpty('supreme')

    def test_results_are_nonempty_when_query_matches_department(self):
        self.login_as_staff()
        self.assertResultsAreNotEmpty('branch')
