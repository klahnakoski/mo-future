from unittest import TestCase

from mo_future import function_type


class TestBasic(TestCase):
    def test_import(self):
        self.assertEqual(function_type, (lambda x: x).__class__)

