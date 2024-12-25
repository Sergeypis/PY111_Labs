import unittest

from task import is_match


class TestIsMatch(unittest.TestCase):
    def test_isMatch(self):
        self.assertEqual(is_match("aa", "a*"), True)
        self.assertEqual(is_match("mississippi", "m??*ss*?i*pi"), False)
        self.assertEqual(is_match("ab", ".*"), False)
        self.assertEqual(is_match("aab", "c*a*b"), False)
        self.assertEqual(is_match("aa", "a"), False)
