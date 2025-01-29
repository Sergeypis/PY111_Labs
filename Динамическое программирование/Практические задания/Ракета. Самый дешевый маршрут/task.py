from functools import lru_cache
from typing import List


# cache_dict: dict[int,dict[int,int]] = {}


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.
    Используется прямой метод со сложностью (M*N).


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    # рассчитать таблицу стоимостей перемещений

    # table = table.copy()
    # n = len(table)
    # m = len(table[0])
    #
    # # Цикл по первому столбцу
    # for row_index in range(n - 1):
    #     table[row_index + 1][0] += table[row_index][0]
    # # Цикл по первой строке
    # for col_index in range(m - 1):
    #     table[0][col_index + 1] += table[0][col_index]
    #
    # for i in range(1, n):
    #     for j in range(1, m):
    #         table[i][j] += min(table[i - 1][j], table[i][j - 1])
    #
    # return table

    total_coasts_tbl = table[:]
    for row in range(len(table) - 1):
        for col in range(len(table[0]) - 1):
            if not row:
                total_coasts_tbl[row][col + 1] += total_coasts_tbl[row][col]
            if not col:
                total_coasts_tbl[row + 1][col] += total_coasts_tbl[row][col]
            total_coasts_tbl[row + 1][col + 1] += min(total_coasts_tbl[row + 1][col], total_coasts_tbl[row][col + 1])

    return total_coasts_tbl

    # def lazy_search_min(table: List[List[int]], row, col):
    #     if not row or not col:
    #         return table[row][col]
    #     if cur_val := cache_dict.get(row, {}).get(col, {}):
    #         return cur_val
    #
    #     h = lazy_search_min(table, row - 1, col)
    #     l = lazy_search_min(table, row, col - 1)
    #     result = table[row][col] + min(h, l)
    #     table[row][col] = result
    #     cache_dict[row][col] = result
    #
    #     return result
    #
    # table = table[:]
    # for row in range(len(table)):
    #     cache_dict[row] = {}
    #
    # for col in range(1, len(table[0])):
    #     table[0][col] += table[0][col - 1]
    # for row in range(1, len(table)):
    #     table[row][0] += table[row - 1][0]
    #
    # a = lazy_search_min(table, row=3-1, col=4-1)
    #
    # return table

def rocket_coasts_recursive_cache(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.
    Используется рекурсивная функция и самописный кэш на словаре.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам или миниммальная стоимость последней клетки
    """
    # рассчитать таблицу стоимостей перемещений

    rows = len(table)
    cols = len(table[0])
    cache: dict[tuple[int,int], int] = {}

    def lazy_search_min(row: int, col: int):
        if (row, col) in cache:
            return cache[(row, col)]

        if row == 0 and col == 0:
            result = table[row][col]
            cache[(row, col)] = result
            return result

        if row == 0:
            result = table[row][col] + lazy_search_min(row, col - 1)
        elif col == 0:
            result = table[row][col] + lazy_search_min(row - 1, col)
        else:
            result = table[row][col] + min(lazy_search_min(row - 1, col), lazy_search_min(row, col - 1))
        cache[(row, col)] = result
        return result

    min_cost = lazy_search_min(rows - 1, cols - 1)
    new_table = [[cache[(i, j)] for i in range(rows)] for j in range(cols)]

    return new_table


def rocket_coasts_recursive_inplace(table: List[List[int]]) -> None:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.
    Используется рекурсивная функция. Таблица состояний формируется во входном массиве.
    @lru_cache обязателен.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам или миниммальная стоимость последней клетки
    """
    # рассчитать таблицу стоимостей перемещений

    rows = len(table)
    cols = len(table[0])

    @lru_cache()
    def lazy_search_min(row: int, col: int):

        if row == 0 and col == 0:
            return table[row][col]

        if row == 0:
            result = table[row][col] + lazy_search_min(row, col - 1)
        elif col == 0:
            result = table[row][col] + lazy_search_min(row - 1, col)
        else:
            result = table[row][col] + min(lazy_search_min(row - 1, col), lazy_search_min(row, col - 1))
        table[row][col] = result

        return result

    min_cost = lazy_search_min(rows - 1, cols - 1)


if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    # total_coasts = rocket_coasts(coasts_ceil)
    # total_coasts = rocket_coasts_recursive_cache(coasts_ceil)
    # print(total_coasts[-1][-1])  # 21
    # print(total_coasts)

    rocket_coasts_recursive_inplace(coasts_ceil)
    print(coasts_ceil)
