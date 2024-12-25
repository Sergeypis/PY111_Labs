import unittest

from task import binary_search


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arr = [i for i in range(100)] + [101]

    def test_existing(self):
        expected_index_list = [5, 23, 54, 78, 91]
        for expected_index in expected_index_list:
            with self.subTest(expected_index=expected_index):
                search_value = expected_index
                self.assertEqual(
                    expected_index, binary_search(search_value, self.arr),
                    msg=f"Неверный индекс искомого значения {search_value}. Ожидается индекс {expected_index}")

    def test_duplicated_values(self):
        expected_index = 1
        search_value = 2
        self.assertEqual(
            expected_index, binary_search(search_value, [1, 2, 2, 2, 2, 2]),
            msg="Бинарный поиск должен возвращать индекс первой встречи искомого элемента"
        )

    def test_missing(self):
        does_not_exists_values_list = [-500, -50, -1, 100, 232, 1000]
        for does_not_exists_value in does_not_exists_values_list:
            with self.subTest(does_not_exists_value=does_not_exists_value):
                with self.assertRaises(ValueError, msg="Если значения нет в последовательности, то должна возвращаться ошибка"):
                    binary_search(does_not_exists_value, self.arr)

    def test_borders(self):
        params = [  # expected_index, search_value, msg
            (0, 0, "Первый элемент не найден. Возможно пропущено уменьшение индекса середины на -1"),
            (100, 101, "Последний элемент не найден. Возможно пропущено увеличение индекса середины на +1"),
        ]
        for expected_index, search_value, msg in params:
            with self.subTest(expected_index=expected_index, search_value=search_value):
                self.assertEqual(
                    expected_index, binary_search(search_value, self.arr),
                    msg=msg
                )

    def test_empty_array(self):
        with self.assertRaises(ValueError, msg="Если значения нет в последовательности, то должна возвращаться ошибка"):
            binary_search(1, [])

    def test_array_with_one_item(self):
        expected_index = 0
        search_value = 100
        self.assertEqual(
            expected_index, binary_search(search_value, [100]),
            msg="Бинарный поиск должен возвращать индекс первой встречи искомого элемента"
        )

    def test_array_with_two_items(self):
        params = [  # expected_index, search_value, msg
            (0, 1000, "Первый элемент не найден. Возможно пропущено уменьшение индекса середины на -1"),
            (1, 1001, "Последний элемент не найден. Возможно пропущено увеличение индекса середины на +1"),
        ]
        for expected_index, search_value, msg in params:
            with self.subTest(expected_index=expected_index, search_value=search_value):
                self.assertEqual(
                    expected_index, binary_search(search_value, [1000, 1001]),
                    msg=msg
                )
