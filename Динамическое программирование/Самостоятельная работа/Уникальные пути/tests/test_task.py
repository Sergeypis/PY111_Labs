import unittest

from task import unique_paths


class TestUniquePaths(unittest.TestCase):
    def test_unique_paths(self):
        self.assertEqual(unique_paths(3, 2), 3)
        self.assertEqual(unique_paths(7, 3), 28)
        self.assertEqual(unique_paths(23, 12), 193536720)
