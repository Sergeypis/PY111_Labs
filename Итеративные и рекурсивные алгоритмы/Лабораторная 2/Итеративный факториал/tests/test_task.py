import unittest
import math

from task import factorial_iterative as factorial


class TestCase(unittest.TestCase):
    def test_fact_iterative(self):
        self.assertEqual(math.factorial(12), factorial(12), msg="Ошибка в расчетах")

    def test_fact_iter_exc(self):
        with self.assertRaises(ValueError, msg="Факториал считается от не отрицательных целых чисел"):
            factorial(-1121)

    def test_fact_rec_exc_float(self):
        with self.assertRaises(TypeError, msg="Факториал считается от не отрицательных целых чисел"):
            factorial(1.74)

    def test_fact_recursive_with_zero(self):
        self.assertEqual(math.factorial(0), factorial(0), msg="Факториал 0 по определению равен 1")
