import unittest
import random

from task import min_search


class TestCase(unittest.TestCase):
    def test_empty_sequence(self):
        empty_seq = []
        with self.assertRaises(ValueError, msg="При поиске минимума в пустой последовательности должна возвращаться ошибка"):
            min_search(empty_seq)

    def test_min(self):
        sequences = [
            [-10, -9, 0],
            [0, 1, 2, 3],
            [i for i in range(3, 10)] + [1],
            [i for i in range(10, -3, -1)],
            [random.randint(-100, 100) for _ in range(300)]
        ]
        for seq in sequences:
            expected_value = min(seq)
            expected_index = seq.index(expected_value)
            with self.subTest(expected_index=expected_index, expected_value=expected_value):
                self.assertEqual(
                    expected_index, min_search(seq),
                    msg=f"Индекс минимального элемента неверный, ожидается: {expected_index}")
