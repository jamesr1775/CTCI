import unittest
from IsPermutationSol2 import IsPermutation
class TestIsUnique(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(IsPermutation("abc", "bca"), True)
    def test_case_2(self):
        self.assertEqual(IsPermutation("abcdd", "abcde"), False)
    def test_case_3(self):
        self.assertEqual(IsPermutation("abc dd aa", "abc dd aa"), True)
    def test_case_4(self):
        self.assertEqual(IsPermutation("abc  d", "abc d"), False)
    def test_case_5(self):
        self.assertEqual(IsPermutation("abc  d> #^$&# .,;", "abc  d> #^$&# .,;"), True)
    def test_case_6(self):
        self.assertEqual(IsPermutation("abc@ d$%^# ", "abc d #$%^"), False)
