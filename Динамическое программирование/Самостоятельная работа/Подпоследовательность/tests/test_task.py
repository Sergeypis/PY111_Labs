import unittest

from task import is_subsequence


class TestIsSubsequence(unittest.TestCase):
    def test_is_subsequence(self):
        self.assertTrue(is_subsequence("abc", "ahbgdc"))
        self.assertFalse(is_subsequence("axc", "ahbgdc"))
        self.assertTrue(is_subsequence("", "ahbgdc"))
        self.assertFalse(is_subsequence("abcd", "ahbgdc"))
        self.assertFalse(is_subsequence("acd", "ahbgdc"))
