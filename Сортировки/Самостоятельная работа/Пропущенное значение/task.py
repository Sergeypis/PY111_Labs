from typing import List


def missing_number(nums: List[int]) -> int:

    if not nums:
        return 0

    end_num = len(nums)
    set_nums = set(val for val in nums)
    for num in range(end_num + 1):
        if num not in set_nums:
            return num

    # Альтернативное решение без доп. памяти
    # n = len(nums)
    #     return n * (n + 1) // 2 - sum(nums)