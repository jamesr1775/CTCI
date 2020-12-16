import unittest
from PalindromePerms import IsPalindromePermutation
class TestIsUnique(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(IsPalindromePermutation("tactcoa"),True)
    def test_case_2(self):
        self.assertEqual(IsPalindromePermutation("tactcoaa"),False)
