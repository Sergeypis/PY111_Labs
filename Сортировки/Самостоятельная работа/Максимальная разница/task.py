import math
from typing import List


def maximum_gap(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    nums.sort()
    min_ = 0
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) > min_:
            min_ = abs(nums[i] - nums[i + 1])
    return min_


    # Альтернативное решение
    # '''
    #     Временная сложность:
    #     лучший: O(N)
    #     худший: O(NlogN)
    #     Сложность по памяти:
    #     O(N)
    #     '''
    # if len(nums) < 2:
    #     return 0
    #
    # nums.sort()
    # max_gap = 0
    # for i in range(1, len(nums)):
    #     max_gap = max(max_gap, nums[i] - nums[i - 1])
    # return max_gap

    # Решение с повышенной сложностью
    # Временная сложность:
    # худший: O(N)
    # Сложность по памяти:
    # O(N)
    # mi, ma, n = min(nums), max(nums), len(nums)
    # if mi == ma:
    #     return 0  # Все элементы одинаковы
    # bucket_size = math.ceil((ma - mi) / (n - 1))  # Определение гипотетического среднего размера ведра
    # min_bucket = [math.inf] * n  # Заполнение явно наибольшими значениями
    # max_bucket = [-math.inf] * n  # Заполнение явно наименьшими значениями
    # for x in nums:
    #     idx = (x - mi) // bucket_size # Определение индекса в какое ведро можно положить значение
    #     min_bucket[idx] = min(min_bucket[idx], x)  # Определение минимального значения в ведре
    #     max_bucket[idx] = max(max_bucket[idx], x)  # Определение максимального значения в ведре
    #
    # max_gap = bucket_size  # Максимальный зазор всегда больше или равен размеру ведра
    # prev = max_bucket[0]
    # for i in range(1, n):
    #     if min_bucket[i] == math.inf:
    #         continue  # Пропуск пустого ведра
    #     max_gap = max(max_gap, min_bucket[i] - prev)
    #     prev = max_bucket[i]
    # return max_gap