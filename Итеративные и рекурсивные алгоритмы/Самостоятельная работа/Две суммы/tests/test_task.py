import unittest

from task import two_sum


class TestTwoSum(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertIn(two_sum(nums, target), [[0, 1], [1, 0]])

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertIn(two_sum(nums, target), [[1, 2], [2, 1]])

    def test_case_3(self):
        nums = [3, 3]
        target = 6
        self.assertIn(two_sum(nums, target), [[0, 1], [1, 0]])