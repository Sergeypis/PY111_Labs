from tokenize import endpats
from typing import List
from unittest.mock import right


# Решение с использованием дополнительной памяти (3 массива), не inplace. Но устойчивая сортировка.

# def sort(container: List[int]) -> List[int]:
#     """
#     Алгоритм быстрой сортировки.
#
#     1. Выбираем опорный элемент. Например, первый элемент.
#     2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
#     3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.
#
#     :param container: последовательность, которую надо отсортировать
#     :return: Отсортированная в порядке возрастания последовательность
#     """
#     # реализовать алгоритм быстрой сортировки
#
#     if len(container) <= 1:
#         return container
#
#     pivot = container[0]
#     left_part = []
#     right_part = []
#     pivot_part = []
#     for num in container:
#         if num < pivot:
#             left_part.append(num)
#         elif num > pivot:
#             right_part.append(num)
#         else:
#             pivot_part.append(num)
#
#     return sort(left_part) + pivot_part + sort(right_part)
#
#     # return (
#     #         sort([item for item in container if item < pivot]) +
#     #         [item for item in container if item == pivot] +
#     #         sort([item for item in container if item > pivot])
#     # )



# Решение inplace на текущей последовательности. Неустойчивое.
def sort(container: List[int], start: int = None, end: int = None) -> None:
    """
    Алгоритм быстрой сортировки inplace.

    1. Выбираем опорный элемент. Средний в массиве.
    2. Идём от краёв массива к центру и сравниваем элементы.Если левый больше правого, меняем местами.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :param start: индекс начала последовательности
    :param end: индекс конца последовательности
    :return: None
    """
    if start is None:
        start = 0
    if end is None:
        end = len(container) - 1
    if start >= end:
        return

    left_idx, right_idx = start, end
    pivot = container[start]

    while left_idx <= right_idx:
        while container[left_idx] < pivot: left_idx += 1
        while container[right_idx] > pivot: right_idx -= 1
        if left_idx <= right_idx:
            container[left_idx], container[right_idx] = container[right_idx], container[left_idx]
            left_idx += 1
            right_idx -= 1

    sort(container, start, right_idx)
    sort(container, left_idx, end)

# [2,3,1] l-4, r-3
# print(sort([2,3,1]))
# sort([4, -3, 1, 2, 5])
container = [4, -3, 1, 2, 5]
sort(container)
print(container)