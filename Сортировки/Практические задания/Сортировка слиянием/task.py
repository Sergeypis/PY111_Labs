from typing import List


# def merge(left_part: List[int], right_part: List[int]) -> List[int]:
#     res = []
#     for _ in range(len(left_part) + len(right_part)):
#         if left_part[0] < right_part[0]:
#             res.append(left_part.pop(0))
#         elif left_part[0] > right_part[0]:
#             res.append(right_part.pop(0))
#         else:
#             res.append(left_part.pop(0))
#             res.append(right_part.pop(0))
#         if not left_part or not right_part:
#             res += left_part + right_part
#             break
#
#     return res

def merge(left_part: List[int], right_part: List[int]) -> List[int]:
    res = []
    idx = 0
    while True:
        if left_part[idx] < right_part[idx]:
            res.append(left_part[idx])
        elif left_part[idx] > right_part[idx]:
            res.append(right_part[idx])
        else:
            res.append(left_part[idx])
            res.append(right_part[idx])
        idx += 1
        if idx == len(left_part) or idx == len(right_part):
            res += left_part + right_part
            break

    return res


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # реализуйте сортировку слиянием

    if len(container) <= 1:
        return container

    middle_idx = len(container) // 2

    left_part = sort(container[:middle_idx])
    right_part = sort(container[middle_idx:])

    return merge(left_part, right_part)


# print(sort([2,1,44,55,3,2,5,6,7,4,5,9,6,33,4,4,4,4]))
print(sort([2,1]))