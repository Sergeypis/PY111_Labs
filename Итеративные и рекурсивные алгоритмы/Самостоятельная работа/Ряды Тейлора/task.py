from turtledemo.penrose import start
from typing import Union
from itertools import count
from math import factorial, pi


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    # вычислить sin(x) с помощью разложения сумму бесконечного ряда

    def item(n):
        """ Подсчет очередного элемента бесконечного ряда Тейлора для sin(x)"""
        return (pow(-1, n)) * (pow(x, 2*n+1)/factorial(2*n+1))

    sum_ = 0
    for i in count():
        current_value = item(i)
        sum_ += current_value

        if abs(current_value) <= DELTA:
            return sum_

print(sinx(pi / 2))