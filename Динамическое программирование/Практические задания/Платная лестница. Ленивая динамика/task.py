import math
import cProfile
from time import sleep
from typing import Union, Sequence
from functools import lru_cache

from line_profiler import profile


@lru_cache()
def stairway_path(stairway: Sequence[Union[float, int]], n=None) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # реализовать ленивую динамику

    if n is None:
        n = len(stairway) - 1
    if n < 0:
        return math.inf
    if n == 0:
        return stairway[0]

    return min(stairway_path(stairway, n - 1), stairway_path(stairway, n - 2)) + stairway[n]


def stairway_path_lazy(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    @lru_cache()
    def lazy_method(stairway, n):
        if n == 0 or n == 1:
            return stairway[n]

        return stairway[n] + min(lazy_method(stairway, n - 1),
                                 lazy_method(stairway, n - 2))

    return lazy_method(stairway, len(stairway) - 1)


if __name__ == '__main__':
    # cProfile.run('print(stairway_path((1, 3, 1, 5)))')  # 7
    print(stairway_path((1, 3, 1, 5)))  # 7
    print(stairway_path_lazy((1, 3, 1, 5)))  # 7


# Измерение времени выполнения построчно с line_profiler
# kernprof -l task.py
# python -m line_profiler task.py.lprof