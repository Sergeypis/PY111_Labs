import unittest

from task import longest_common_prefix


class TestSolution(unittest.TestCase):
    def test_longestCommonPrefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longest_common_prefix(["dog"]), "dog")
        self.assertEqual(longest_common_prefix([]), "")
