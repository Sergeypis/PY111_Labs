from typing import Sequence
from functools import reduce
import sys


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # реализовать алгоритм сортировки подсчетами

    if not container:
        return container
    max_val = max(container)
    temp_list = [0] * (max_val + 1)
    res = []

    for val in container:
        temp_list[val] += 1

    # for idx, val in enumerate(temp_list):
    #     if val != 0:
    #         res.extend([idx] * val)

    # data_gen = ([idx] * val for idx, val in enumerate(temp_list) if val > 0)
    # data_list = [[idx] * val for idx, val in enumerate(temp_list) if val > 0]
    # print(sys.getsizeof(data_gen), sys.getsizeof(data_list))

    return reduce(lambda x, y: x+y, ([idx] * val for idx, val in enumerate(temp_list) if val > 0))
    return [[idx] * val for idx, val in enumerate(temp_list) if val > 0]
    # return res

print(sort([3,0,1,6,4,22,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]))