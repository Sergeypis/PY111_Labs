import unittest

from task import longest_increasing_path


class TestSolution(unittest.TestCase):
    def test_longest_increasing_path(self):
        self.assertEqual(longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]]), 4)
        self.assertEqual(longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]]), 4)
