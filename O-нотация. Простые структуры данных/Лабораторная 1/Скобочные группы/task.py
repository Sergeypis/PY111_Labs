from typing import Any


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, elem: Any) -> None:
        self.__stack.append(elem)

    def pop(self) -> Any:
        if len(self.__stack):
            return self.__stack.pop(-1)
        else:
            raise IndexError("Error, stack is empty!")

    def peek(self, ind: int) -> Any:
        if not isinstance(ind, int):
            raise TypeError(f"Error type index: {type(ind).__name__}")
        if not 0 <= ind < len(self.__stack):
            raise IndexError(f"Index {ind=} out of range!")
        ind = -1 - ind
        return self.__stack[ind]

    def clear(self) -> None:
        self.__stack.clear()

    def __len__(self) -> int:
        return len(self.__stack)


def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    stack = Stack()
    for symbol in brackets_row:
        if symbol in ['(', ')']:
            if symbol == '(':
                stack.push(symbol)
            else:
                if not stack.__len__():
                    return False
                stack.pop()
    return False if stack.__len__() else True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets("((fff)sdcv()())"))  # True
