import unittest

from task import num_decodings


class TestSolution(unittest.TestCase):
    def test_num_decodings(self):
        self.assertEqual(num_decodings("12"), 2)
        self.assertEqual(num_decodings("226"), 3)
        self.assertEqual(num_decodings("0"), 0)
        self.assertEqual(num_decodings("10"), 1)
        self.assertEqual(num_decodings("101"), 1)
