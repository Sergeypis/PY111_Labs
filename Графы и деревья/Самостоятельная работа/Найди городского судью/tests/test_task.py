import unittest

from task import find_judge


class TestSolution(unittest.TestCase):
    def test_find_judge(self):
        self.assertEqual(find_judge(2, [[1, 2]]), 2)
        self.assertEqual(find_judge(3, [[1, 3], [2, 3]]), 3)
        self.assertEqual(find_judge(3, [[1, 3], [2, 3], [3, 1]]), -1)
        self.assertEqual(find_judge(3, [[1, 2], [2, 3]]), -1)
        self.assertEqual(find_judge(1, []), 1)
