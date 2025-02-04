from functools import reduce
from typing import List

import random


# 2. Считалочка

def counting(n: int, k: int) -> int:
    """
    Считалка начинает считать с первого человека.
    Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
    Игра происходит до тех пор, пока не останется последний человек.
    Для данных N и К дать номер последнего оставшегося человека.

    :param n: Количество человек в игре.
    :param k: Количество слогов в считалке.
    :return: Номер последнего оставшегося человека.
    """

    i, w = 0, 0
    humans = [m for m in range(1, n + 1)]
    while len(humans) != 1:
        if humans[w]:
            i += 1
            if i == k:
                humans.pop(w)
                i = 0
                w -= 1
            w += 1
            if w == len(humans):
                w = 0
    return humans[0]


# 3. Посчитать число компонент связности графа


# 8. Сортировка
def counting_sort(mass: List[int]) -> List[int]:
    """
    Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
    Задача: отсортировать массив наиболее эффективным способом

    :param mass: массив из 10**6 целых чисел
    :return: отсортированный массив
    """
    diff = MAX_NUM - MIN_NUM
    temp_list = [0] * diff
    if not mass:
        return []
    for val in mass:
        temp_list[val - MIN_NUM - 1] += 1

    return reduce(lambda x, y: x+y, ([idx + MIN_NUM] * val for idx, val in enumerate(temp_list) if val > 0))


if __name__ == '__main__':
    # print(counting(n=90, k=5))  # 2.

    MIN_NUM = 13
    MAX_NUM = 26
    LENGTHS = 10 ** 6
    mass: List[int] = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LENGTHS)]
    print(counting_sort(mass))