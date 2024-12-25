import unittest

from task import fib_iterative as fib


class TestCase(unittest.TestCase):
    def test_fib_numbers(self):
        fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
        for fib_num_index, fib_num in enumerate(fib_numbers):
            with self.subTest(fib_num_index=fib_num_index, fib_num=fib_num):
                self.assertEqual(
                    fib_num, fib(fib_num_index),
                    msg=f"Не правильно :( {fib_num_index}-е число фибоначчи должно быть {fib_num}. Ты помнишь, что нумерация должна начинаться с 0?"
                )

    def test_fib_from_negative_index(self):
        with self.assertRaises(ValueError, msg="Что такое -35 число фибоначчи? Должна вызываться ошибка"):
            fib(-35)
