from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    # найти количество маршрутов до каждой ступени

    if count_stairs < 0:
        raise ValueError("Ошибка. Количество ступеней не может быть отрицательным.")

    state = []
    for n in range(count_stairs + 1):
        if n == 0:
            state.append(0)
        elif n == 1:
            state.append(1)
        else:
            state.append(state[n - 1] + state[n - 2])

    return state


if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
