"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        # self.deque = deque  # TODO использовать deque для реализации очереди с приоритетами
        self.queue_pr: dict[int, deque] = {}  # Словарь очередей с приоритетом

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемента в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        if not isinstance(priority, int):
            raise TypeError(f"Error, priority must be integer, but not {type(priority).__name__}")
        if not self.HIGH_PRIORITY <= priority <= self.LOW_PRIORITY:
            raise IndexError("Queue priority out of range")

        deq = self.queue_pr.get(priority, None)
        if deq is None:
            deq = deque()
            deq.append(elem)
            self.queue_pr[priority] = deq
        else:
            deq.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """

        if self.__len__():
            priority = min(self.queue_pr)
            diq = self.queue_pr.get(priority)
            elem = diq.popleft()
            if not len(diq): del self.queue_pr[priority]
            return elem
        else:
            raise IndexError("Error, queue is empty!")

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(priority, int):
            raise TypeError(f"Error, priority must be integer, but not {type(priority).__name__}")
        if not self.HIGH_PRIORITY <= priority <= self.LOW_PRIORITY:
            raise IndexError("Queue priority out of range")

        if not isinstance(ind, int):
            raise TypeError(f"Error, Index must be integer, but not {type(ind).__name__}")

        diq = self.queue_pr.get(priority, None)
        if diq is None:
            raise IndexError("Нет элементов с таким приоритетом")
        if not 0 <= ind < len(diq):
            raise IndexError("Queue index out of range")

        return diq[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        self.queue_pr.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        return sum([len(diq) for diq in self.queue_pr.values()])
