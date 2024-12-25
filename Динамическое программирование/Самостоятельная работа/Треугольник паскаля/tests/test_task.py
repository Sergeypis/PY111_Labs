import unittest

from task import generate


class TestSolution(unittest.TestCase):
    def test_generate(self):
        self.assertEqual(generate(0), [])
        self.assertEqual(generate(1), [[1]])
        self.assertEqual(generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

