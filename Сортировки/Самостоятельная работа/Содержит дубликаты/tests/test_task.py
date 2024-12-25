import unittest

from task import contains_duplicate


class TestContainsDuplicate(unittest.TestCase):

    def test_contains_duplicate(self):
        nums = [1, 2, 3, 1]
        result = contains_duplicate(nums)
        self.assertTrue(result)

        nums = [1, 2, 3, 4]
        result = contains_duplicate(nums)
        self.assertFalse(result)

        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        result = contains_duplicate(nums)
        self.assertTrue(result)

    def test_empty_input(self):
        nums = []
        result = contains_duplicate(nums)
        self.assertFalse(result)
