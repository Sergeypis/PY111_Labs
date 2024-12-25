import unittest

from task import Queue


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.my_queue = Queue()

    def setUp(self):
        self.my_queue.clear()

    def test__len__(self):
        self.assertTrue(hasattr(self.my_queue, "__len__"), msg="Очередь должна иметь магический метод __len__ для определения размера очереди.")

    def test_clear(self):
        self.my_queue.enqueue(3)
        self.my_queue.clear()

        self.assertEqual(0, len(self.my_queue), msg="Точно ли очередь была очищена???")

    def test_dequeue_empty_queue(self):
        with self.assertRaises(IndexError, msg="Если в очереди нет элементов, то dequeue должен вернуть ошибку"):
            self.my_queue.dequeue()

    def test_enqueue_dequeue(self):
        initial_elem = 3
        self.my_queue.enqueue(initial_elem)

        self.assertEqual(
            initial_elem, self.my_queue.dequeue(),
            msg="Некорректно работают операции dequeue или enqueue"
        )

    def test_multiple_en_de_queues(self):
        expected_values = list(range(5))
        for value in expected_values:
            self.my_queue.enqueue(value)

        for ind, expected_value in enumerate(expected_values):
            with self.subTest(ind=ind, expected_value=expected_value):
                self.assertEqual(
                    expected_value, self.my_queue.dequeue(),
                    msg=f"Ожидается значение {expected_value}. Очередь работает по принципу FIFO - первый пришел первый вышел"
                )

        self.assertEqual(0, len(self.my_queue), msg="Очередь должна быть пустой")

    def test_peek(self):
        expected_values = [5, 3, 7]
        for value in expected_values:
            self.my_queue.enqueue(value)

        for ind, expected_value in enumerate(expected_values):
            with self.subTest(ind=ind, expected_value=expected_value):
                self.assertEqual(
                    expected_value, self.my_queue.peek(ind),
                    msg=f"Ожидается значение {expected_value}"
                )

        self.assertEqual(len(expected_values), len(self.my_queue), msg="Очередь не должна быть пустой")

    def test_peek_default_ind(self):
        expected_values = [5, 3, 7]
        for value in expected_values:
            self.my_queue.enqueue(value)

        self.assertEqual(
            self.my_queue.peek(), expected_values[0],
            msg="По умолчанию peep должен возвращать элемент с начала очереди"
        )
