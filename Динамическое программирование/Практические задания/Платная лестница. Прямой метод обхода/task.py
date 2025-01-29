import math
from typing import Union, Sequence
import timeit


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # реализовать прямой метод расчета

    len_ = len(stairway)
    if len_ < 1:
        raise ValueError("Ошибка. Не может быть 0 ступеней")
    elif len_ == 1:
        return stairway[0]

    n_1 = stairway[0]
    n_2 = 0
    for stage in range(1, len_):
        n_2 = min(n_1, n_2) + stairway[stage]
        n_1, n_2 = n_2, n_1

    return n_1


if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5]))  # 7
