import unittest
import math

from task import sinx, DELTA


class TestCase(unittest.TestCase):
    def test_sinx(self):
        const = 1.55433
        self.assertAlmostEqual(
            math.sin(const), sinx(const), delta=DELTA,
            msg="Нужно больше точности :D"
        )
