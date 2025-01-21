from typing import List


def contains_duplicate(nums: List[int]) -> bool:

    if not nums:
        return False
    return True if len(set(nums)) != len(nums) else False
    # return len(nums) > len(set(nums))