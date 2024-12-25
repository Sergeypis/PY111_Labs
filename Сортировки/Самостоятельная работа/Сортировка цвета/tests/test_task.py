import unittest

from task import sort_сolors


class TestSortColors(unittest.TestCase):
    def test_sortColors(self):
        nums = [2, 0, 2, 1, 1, 0]
        sort_сolors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

        nums = [1, 2, 0]
        sort_сolors(nums)
        self.assertEqual(nums, [0, 1, 2])

        nums = [2, 2, 2, 1, 1, 0, 0, 0]
        sort_сolors(nums)
        self.assertEqual(nums, [0, 0, 0, 1, 1, 2, 2, 2])
