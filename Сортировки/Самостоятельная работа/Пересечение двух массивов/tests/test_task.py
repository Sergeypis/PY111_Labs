import unittest

from task import intersection


class TestIntersection(unittest.TestCase):
    def test_intersection(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        result = intersection(nums1, nums2)
        self.assertEqual(result, [2])

        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        result = intersection(nums1, nums2)
        self.assertIn(result, [[9, 4], [4, 9]])

        nums1 = []
        nums2 = []
        result = intersection(nums1, nums2)
        self.assertEqual(result, [])
