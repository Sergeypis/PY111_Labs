import unittest

from task import majority_element


class TestMajorityElement(unittest.TestCase):

    def test_majority_element(self):
        nums = [3, 2, 3]
        result = majority_element(nums)
        self.assertEqual(result, 3)

        nums = [2, 2, 1, 1, 1, 2, 2]
        result = majority_element(nums)
        self.assertEqual(result, 2)

        nums = [1, 1, 2, 2, 2, 2, 3, 3, 3, 2, 2]
        result = majority_element(nums)
        self.assertEqual(result, 2)

    def test_empty_input(self):
        nums = []
        result = majority_element(nums)
        self.assertIsNone(result)
