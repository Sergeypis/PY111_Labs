import unittest
import random

from task import sort


class TestCase(unittest.TestCase):
    def test_sorted(self):
        arr = [random.randint(0, 10) for _ in range(random.randint(50, 60))]
        self.assertEqual(
            sorted(arr), sort(arr),
            msg="Последовательность не отсортировалась"
        )

    def test_sort_empty_seq(self):
        empty_arr = []
        self.assertEqual(
            empty_arr, sort(empty_arr),
            msg="Пустая последовательность должна сортироваться :)"
        )

    def test_sort_one_item(self):
        one_item_seq = [1]
        self.assertEqual(
            one_item_seq, sort(one_item_seq),
            msg="Почему-то не отсортировалась последовательность из одного элемента :("
        )
