from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    ...

    res: List[int] = []
    set_nums1 = set(val for val in nums1)
    for num in nums2:
        if num in set_nums1:
            res.append(num)
            set_nums1.remove(num)
    return res

    # Альтернативное решение
    # set1 = set(nums1)
    # set2 = set(nums2)
    # return list(set1 & set2)