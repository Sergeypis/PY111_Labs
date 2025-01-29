from unittest import TestCase

from ..task import rocket_coasts_recursive_inplace

class TestTime(TestCase):
    def timeit_(self):
        coasts_ceil = [
            [2, 7, 9, 3],
            [12, 4, 1, 9],
            [1, 5, 2, 5]
        ]
        res = [
            [2, 9, 18, 21],
            [14, 13, 14, 23],
            [15, 18, 16, 21]
        ]
        rocket_coasts_recursive_inplace(coasts_ceil)
        self.assertEqual(coasts_ceil, res)

