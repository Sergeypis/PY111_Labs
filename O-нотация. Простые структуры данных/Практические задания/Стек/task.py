from typing import Any


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
        self._stack.append(elem)

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        if len(self._stack):
            return self._stack.pop()  # реализовать операцию pop
        else:
            raise IndexError("Error, stack is empty!")

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент, 1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):  # реализовать операцию peek
            raise TypeError(f"Error, Index must be integer, but not {type(ind).__name__}")
        if not 0 <= ind < len(self._stack):
            raise IndexError("Stack index out of range")

        ind = -1 - ind

        return self._stack[ind]

    def clear(self) -> None:
        """ Очистка стека. """
        self._stack.clear()  # реализовать операцию clear

    def __len__(self) -> int:
        """ Количество элементов в стеке. """
        return len(self._stack) # реализовать операцию __len__


if __name__ == '__main__':

    st = Stack()

    st.push(1)
    st.push(3)
    st.push(5)

    st.peek()
