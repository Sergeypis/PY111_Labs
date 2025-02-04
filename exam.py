from functools import reduce
from typing import List
import networkx as nx

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


# 4. Навигатор на сетке

def build_graph(grid):
    G = nx.DiGraph()
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # print((row, col), (new_row, new_col), grid[new_row][new_col])
                    G.add_edge((row, col), (new_row, new_col), weight=grid[new_row][new_col])

    return G

def find_min_cost_path(
        grid: List[List[int]],
        start: tuple[int, int],
        end: tuple[int, int]
) -> tuple[int, List[tuple[int, int]]]:
    """
    Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку
    (все стоимости положительные). Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку
    и вывести этот путь.

    :param grid: Массив
    :param start: Начальная ячейка
    :param end: Конечная ячейка
    :return:
    """
    G = build_graph(grid)
    min_cost = nx.dijkstra_path_length(G, start, end, weight='weight')
    path = nx.dijkstra_path(G, start, end, weight='weight')
    return min_cost, path

# 7. Аренда ракет

def rocket_rental(rent_list: List[tuple[int, int]]) -> bool:
    """
    Каждый день к вам приходит список заявок на использование ракет в виде:
    [(2, 3), (3, 7), (8, 9), (1, 2), (9, 15), (23, 24), (16, 20)]. Вывести ответ, хватит ли вам одной ракеты,
    чтобы удовлетворить все заявки на этот день

    :param rent_list: Список заявок
    :return: True или False
    """
    rent_list.sort(key=lambda x: x[1])
    app_end = 0
    for start, end in rent_list:
        if app_end > start:
            return False
        app_end = end

    return True


if __name__ == '__main__':
# 2. Считалочка
    # print(counting(n=90, k=5))

# 8. Сортировка
    # MIN_NUM = 13
    # MAX_NUM = 26
    # LENGTHS = 10 ** 6
    # mass: List[int] = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LENGTHS)]
    # print(counting_sort(mass))

# 4. Навигатор на сетке
#     grid = [
#         [1, 3, 1],
#         [1, 5, 1],
#         [4, 2, 1]
#     ]
#     start = (0, 0)
#     end = (2, 1)
#
#     min_cost, path = find_min_cost_path(grid, start, end)
#     print(f"Минимальная стоимость пути: {min_cost}")
#     print(f"Путь: {path}")

# 7. Аренда ракет
#     rent_list = [(2, 3), (3, 7), (4, 6), (1, 2)]
    rent_list = [(2, 3), (3, 7), (8, 9), (1, 2), (9, 15), (23, 24), (16, 20)]
    res = rocket_rental(rent_list)
    print(f"Одна ракета удовлетворит все заяыки на этот день: {res}")