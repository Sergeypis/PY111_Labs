import unittest

from task import trap


class TestTrap(unittest.TestCase):
    def test_trap(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap([4, 2, 0, 3, 2, 4, 3, 4]), 10)
        self.assertEqual(trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]), 23)
        self.assertEqual(trap([2, 0, 2]), 2)
        self.assertEqual(trap([3, 0, 0, 2, 0, 4]), 10)
