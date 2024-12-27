"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        Начало слева.
        """
        self.queue = [any] # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:  # O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.append(elem)

    def dequeue(self) -> Any:  # O(N)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if len(self.queue):
            return self.queue.pop(0)
        raise IndexError("Error, queue is empty!")

    def peek(self, ind: int = 0) -> Any:  # O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Type error, ind must be integer")
        if not 0 <= ind < len(self.queue):
            raise IndexError("Queue priority out of range")

        return self.queue[ind]

    def clear(self) -> None:  # O(1)
        """ Очистка очереди. """
        self.queue.clear()

    def __len__(self):  # O(1)
        """ Количество элементов в очереди. """
        return len(self.queue)
