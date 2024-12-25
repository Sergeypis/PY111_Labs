import unittest

from task import missing_number


class TestMissingNumber(unittest.TestCase):
    def test_missing_number(self):
        nums = [3, 0, 1]
        result = missing_number(nums)
        self.assertEqual(result, 2)

        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        result = missing_number(nums)
        self.assertEqual(result, 8)

        nums = [0]
        result = missing_number(nums)
        self.assertEqual(result, 1)
