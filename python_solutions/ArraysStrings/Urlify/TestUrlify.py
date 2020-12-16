import unittest
from Urlify import Urlify
class TestIsUnique(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Urlify("Mr John Smith    ", 13), "Mr%20John%20Smith")
