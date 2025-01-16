from typing import List

# Решение с выбороркой элементов из массивов при слиянии
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


# Решение с работой на указателях в массивах без использования операций удаления из массивов, что влечет перезапись массивов в памяти
def merge(left_part: List[int], right_part: List[int]) -> List[int]:
    res = []
    idx_left = 0
    idx_right = 0
    max_idx_l = len(left_part)
    max_idx_r = len(right_part)
    while idx_left != max_idx_l and idx_right != max_idx_r:
        if left_part[idx_left] > right_part[idx_right]:
            res.append(right_part[idx_right])
            idx_right += 1
            if idx_right == max_idx_r:
                return res + left_part[idx_left:]
        elif left_part[idx_left] < right_part[idx_right]:
            res.append(left_part[idx_left])
            idx_left += 1
            if idx_left == max_idx_l:
                return res + right_part[idx_right:]
        else:
            res.append(left_part[idx_left])
            res.append(right_part[idx_right])
            idx_right += 1
            idx_left += 1

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


print(sort([2,1,44,55,3,2,5,6,7,4,5,9,6,33,4,4,4,4]))
# print(sort([2,1]))