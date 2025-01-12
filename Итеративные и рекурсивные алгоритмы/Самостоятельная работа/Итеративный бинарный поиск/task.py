from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    # реализовать итеративный алгоритм бинарного поиска

    # low_ind = 0
    # high_ind = len(seq) - 1
    # while low_ind <= high_ind:
    #     mid_ind = low_ind + ((high_ind - low_ind) // 2)
    #     if value == seq[mid_ind]:
    #         while value == seq[mid_ind]:
    #             mid_ind -= 1
    #             if mid_ind < 0:
    #                 break
    #         return mid_ind + 1
    #     elif value < seq[mid_ind]:
    #         high_ind = mid_ind - 1
    #     else:
    #         low_ind = mid_ind + 1
    # raise ValueError("Error! Value is missing from the sequence.")

    low_ind = 0
    high_ind = len(seq) - 1
    ind = None

    while low_ind <= high_ind:
        mid_ind = low_ind + ((high_ind - low_ind) // 2)
        if value == seq[mid_ind]:
            ind = mid_ind
            high_ind = mid_ind -1
        elif value < seq[mid_ind]:
            high_ind = mid_ind - 1
        else:
            low_ind = mid_ind + 1
    if ind is None:
        raise ValueError("Error! Value is missing from the sequence.")
    return ind