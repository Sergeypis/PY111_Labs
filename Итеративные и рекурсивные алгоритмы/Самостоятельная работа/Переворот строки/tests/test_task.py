import unittest

from task import reverse_string


class TestReverseString(unittest.TestCase):
    def test_case_1(self):
        input = ["h","e","l","l","o"]
        expected_output = ["o","l","l","e","h"]
        reverse_string(input)
        self.assertEqual(input, expected_output)

    def test_case_2(self):
        input = ["H","a","n","n","a","h"]
        expected_output = ["h","a","n","n","a","H"]
        reverse_string(input)
        self.assertEqual(input, expected_output)

    def test_case_3(self):
        input = []
        expected_output = []
        reverse_string(input)
        self.assertEqual(input, expected_output)
