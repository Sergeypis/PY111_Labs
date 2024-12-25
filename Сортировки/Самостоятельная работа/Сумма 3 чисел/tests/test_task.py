import unittest

from task import three_sum


class TestThreeSum(unittest.TestCase):
    def test_example_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected_result = [[-1, -1, 2], [-1, 0, 1]]
        result = three_sum(nums)
        self.assertEqual(result, expected_result)

    def test_example_2(self):
        nums = [0, 0, 0]
        expected_result = [[0, 0, 0]]
        result = three_sum(nums)
        self.assertEqual(result, expected_result)

    def test_example_3(self):
        nums = []
        expected_result = []
        result = three_sum(nums)
        self.assertEqual(result, expected_result)