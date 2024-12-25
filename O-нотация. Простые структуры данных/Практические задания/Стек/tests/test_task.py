import unittest

from task import Stack


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.my_stack = Stack()

    def setUp(self):
        self.my_stack.clear()

    def test__len__(self):
        self.assertTrue(hasattr(self.my_stack, "__len__"), msg="Стек должен иметь магический метод __len__ для определения размера стека.")

    def test_clear(self):
        self.my_stack.push(3)
        self.my_stack.clear()

        self.assertEqual(0, len(self.my_stack), msg="Точно ли стек был очищен???")

    def test_empty_stack(self):
        with self.assertRaises(IndexError, msg="Если в стеке нет элементов, то pop должен вернуть ошибку"):
            self.my_stack.pop()

    def test_push_pop(self):
        initial_elem = 3
        self.my_stack.push(initial_elem)

        self.assertEqual(
            initial_elem, self.my_stack.pop(),
            msg="Некорректно работают операции push или pop"
        )

    def test_multiple_pushes_pops(self):
        expected_values = list(range(4, 0, -1))
        for value in expected_values[::-1]:
            self.my_stack.push(value)

        for ind, expected_value in enumerate(expected_values):
            with self.subTest(ind=ind, expected_value=expected_value):
                self.assertEqual(
                    expected_value, self.my_stack.pop(),
                    msg=f"Ожидается значение {expected_value}. Стек работает по принципу LIFO - последний пришел первый вышел"
                )

        self.assertEqual(0, len(self.my_stack), msg="Стек должен быть пустым")

    def test_peek(self):
        expected_values = [5, 3, 7]
        for value in expected_values[::-1]:
            self.my_stack.push(value)

        for ind, expected_value in enumerate(expected_values):
            with self.subTest(ind=ind, expected_value=expected_value):
                self.assertEqual(
                    expected_value, self.my_stack.peek(ind),
                    msg=f"Ожидается значение {expected_value}"
                )

        self.assertEqual(len(expected_values), len(self.my_stack), msg="Стек не должен быть пустым")

    def test_peek_default_ind(self):
        expected_values = [5, 3, 7]
        for value in expected_values:
            self.my_stack.push(value)

        self.assertEqual(
            self.my_stack.peek(), expected_values[-1],
            msg="По умолчанию peep должен возвращать элемент с вершины"
        )

    def test_peek_out_of_range_ind(self):
        expected_values = [5, 3, 7]
        for value in expected_values:
            self.my_stack.push(value)

        with self.assertRaises(TypeError, msg="peek работает только с целочисленными индексами"):
            self.my_stack.peek("incorrect_type_ind")

        with self.assertRaises(IndexError, msg="Если указан неверный индекс, то должна вызываться ошибка"):
            out_of_range_index = len(self.my_stack)
            self.my_stack.peek(out_of_range_index)
