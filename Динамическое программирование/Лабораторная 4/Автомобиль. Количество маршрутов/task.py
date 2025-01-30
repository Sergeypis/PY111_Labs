from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # решить задачу с помощью динамического программирования

    # state_tbl = [[0 for _ in range(m)] for _ in range(n)]
    state_tbl = [[0]*m for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if row == 0 or col == 0:
                state_tbl[row][col] = 1
            else:
                state_tbl[row][col] = state_tbl[row - 1][col - 1] + state_tbl[row - 1][col] + state_tbl[row][col - 1]

    return state_tbl


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
