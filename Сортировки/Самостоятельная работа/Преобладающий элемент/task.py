from typing import List


def majority_element(nums: List[int]) -> int:

    if not nums:
        return None
    m_e = 0
    count = 0
    for num in nums:
        if count == 0:
            m_e = num
            count = 1
        elif num == m_e:
            count += 1
        else:
            count -= 1
    return m_e

print(majority_element([1,5,3,3,3,3,3,1,1,5,5,5]))