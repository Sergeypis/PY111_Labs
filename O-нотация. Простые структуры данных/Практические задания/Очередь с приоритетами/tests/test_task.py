import unittest

from task import PriorityQueue


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.my_priority_queue = PriorityQueue()

    def setUp(self):
        self.my_priority_queue.clear()

    def test__len__(self):
        self.assertTrue(hasattr(self.my_priority_queue, "__len__"), msg="Очередь должна иметь магический метод __len__ для определения размера очереди.")

    def test_clear(self):
        self.my_priority_queue.enqueue(3)
        self.my_priority_queue.clear()

        self.assertEqual(0, len(self.my_priority_queue), msg="Точно ли очередь была очищена???")

    def test_dequeue_empty_queue(self):
        with self.assertRaises(IndexError, msg="Если в очереди нет элементов, то dequeue должен вернуть ошибку"):
            self.my_priority_queue.dequeue()

    def test_enqueue_dequeue_without_priority(self):
        initial_elem = 3
        self.my_priority_queue.enqueue(initial_elem)

        self.assertEqual(initial_elem, self.my_priority_queue.dequeue())

    def test_multiple_en_de_queues_without_priority(self):
        items = [i for i in range(10)]

        for i in items:
            self.my_priority_queue.enqueue(i)

        received_items = []
        for _ in items:
            received_items.append(self.my_priority_queue.dequeue())

        self.assertEqual(items, received_items)

    def test_peek(self):
        self.my_priority_queue.enqueue(3)
        self.my_priority_queue.enqueue(5)
        self.my_priority_queue.enqueue(7)

        self.assertEqual(3, self.my_priority_queue.peek())
        self.assertEqual(5, self.my_priority_queue.peek(1))
        self.assertEqual(3, self.my_priority_queue.peek())

    def test_en_de_queue_with_priority(self):
        high_priority = 0
        medium_priority = 5
        low_priority = 10
        self.my_priority_queue.enqueue(10, high_priority)
        self.my_priority_queue.enqueue(0, low_priority)

        self.assertEqual(10, self.my_priority_queue.dequeue())

        self.my_priority_queue.enqueue(1, low_priority)
        self.my_priority_queue.enqueue(5, medium_priority)

        self.assertEqual(5, self.my_priority_queue.dequeue())
        self.assertEqual(0, self.my_priority_queue.dequeue())
        self.assertEqual(1, self.my_priority_queue.dequeue())