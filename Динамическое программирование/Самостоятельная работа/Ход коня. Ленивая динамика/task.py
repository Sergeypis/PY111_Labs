from typing import Tuple
from functools import lru_cache


def calculate_paths(shape: Tuple[int, int]) -> int:
    """
    Дано поле с размером rows*cols посчитать количество ходов коня из верхнего левого угла в нижний правый

    :param shape: размер доски в виде кортежа
    :return: количество путей согласно заданным условиям
    """
    ... # TODO реализуйте подсчет ходов коня


if __name__ == '__main__':
    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths((7, 15)))  # 13309
