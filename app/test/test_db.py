from django.test import TestCase

from app.models import *


class MigrateTestCase(TestCase):
    '''Another dumb to make sure the test db works.'''
    @classmethod
    def setUpTestData(cls):
        cls.john = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

    def test_migrate(self):
        NaturalPerson.objects.create(person_id=self.john, name='john')
