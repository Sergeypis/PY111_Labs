from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    ...  # TODO найти количество маршрутов до каждой ступени


if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
