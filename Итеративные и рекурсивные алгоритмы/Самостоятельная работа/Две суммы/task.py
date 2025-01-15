from typing import List
from collections import defaultdict


def two_sum(nums: List[int], target: int) -> List[int]:

    # for ind_1, val_1 in enumerate(nums[:-1]):
    #     for ind_2, val_2 in enumerate(nums[ind_1 + 1:], ind_1 + 1):
    #         if target == val_1 + val_2:
    #             return [ind_1, ind_2]
    # return None

    # dict_ = {target - val: idx for idx, val in enumerate(nums)}
    # for idx, val in enumerate(nums):
    #     if dict_.get(val) and not dict_[val] == idx:
    #         return [dict_[val], idx]

    # dict_ = {target - val: idx for idx, val in enumerate(nums)}
    # for key, idx in dict_.items():
    #     if num := dict_.get(target - key):
    #         return [num, dict_[key]]

    dict_ = defaultdict(list)
    list(dict_[target - val].append(idx) for idx, val in enumerate(nums))  # {5:[0],3:[1,2],2:[3]}
    for key, idx in dict_.items():
        num = dict_.get(target - key)
        if num and num[0] != idx[0]:
            if target - key == key and len(num) > 1:
                num = [num[1]]
            return [dict_[key][0], *num]

print(two_sum([0,3,3,2,5], 6))