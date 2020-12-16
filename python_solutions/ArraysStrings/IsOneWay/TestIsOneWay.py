import unittest
from IsOneWay import IsOneWay 

class TestIsOneWay(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(IsOneWay("pale", "ple"), True)
    def test_case_2(self):
        self.assertEqual(IsOneWay("abcdd", "abcdde"), True)
    def test_case_3(self):
        self.assertEqual(IsOneWay("abcdd", "abcdd"), True)
    def test_case_4(self):
        self.assertEqual(IsOneWay("abcdd", "acbcdde"), False)
