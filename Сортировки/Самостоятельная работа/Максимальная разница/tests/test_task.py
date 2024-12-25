import unittest

from task import maximum_gap


class TestSolution(unittest.TestCase):
    def test_maximum_gap(self):
        self.assertEqual(maximum_gap([3, 6, 9, 1]), 3)
        self.assertEqual(maximum_gap([10]), 0)
        self.assertEqual(maximum_gap([1, 1, 1, 1]), 0)
        self.assertEqual(maximum_gap([1, 2, 3, 4, 5, 6, 7, 8, 9]), 1)