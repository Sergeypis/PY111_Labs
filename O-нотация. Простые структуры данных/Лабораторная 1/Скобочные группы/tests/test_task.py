import unittest

from task import check_brackets


class TestCase(unittest.TestCase):
    def test_invalid(self):
        incorrect_brackets_list = ["(()(", "(()))", "(()))", ")(", ")()("]
        for brackets in incorrect_brackets_list:
            with self.subTest(brackets=brackets):
                self.assertFalse(check_brackets(brackets))

    def test_valid(self):
        incorrect_brackets_list = ["", "()()", "(()())", "((()(())()))()"]
        for brackets in incorrect_brackets_list:
            with self.subTest(brackets=brackets):
                self.assertTrue(check_brackets(brackets))
