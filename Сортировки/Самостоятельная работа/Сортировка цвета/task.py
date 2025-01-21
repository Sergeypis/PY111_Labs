from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """
    # Сортировка пузырьком
    n = 1
    while n < len(nums):
        for i in range(len(nums) - n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        n += 1

    # Альтернативное решение за О(N).
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1