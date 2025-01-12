"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # реализовать итеративный линейный поиск
    if not arr:
        raise ValueError("Error! List is empty.")
    index_min_num = 0
    min_num = arr[index_min_num]
    for ind, num in enumerate(arr[1:], 1):
        if num < min_num:
            min_num = num
            index_min_num = ind
    return index_min_num

print(min_search([0]))