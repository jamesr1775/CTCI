import unittest
from IsUnique import IsUnique

class TestIsUnique(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(IsUnique("abc"), True)
    def test_case_2(self):
        self.assertEqual(IsUnique("abcdd"), False)

