"""
1. Бинарный поиск итеративный
"""
def binary_search(arr, item):
    n = 0
    min_idx = 0
    max_idx = len(arr) - 1
    while min_idx <= max_idx:
        mid = (max_idx + min_idx)//2  # min_idx + ((max_idx - min_idx) // 2)
        if item == arr[mid]:
            print(f"Число операций: {n}")
            return mid
        elif item < arr[mid]:
            max_idx = mid - 1
        else:
            min_idx = mid + 1
        n += 1
    return  None

"""
2. Сортировка выбором
"""
def find_smallest(arr):
    """ Поиск наименьшего в массиве """
    smallest_idx = 0
    smallest = arr[smallest_idx]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

def selection_sort(arr):
    """ Функция сортировки выбором по возрастанию """
    sorted_arr = []
    copy_arr = list(arr)
    for _ in range(len(copy_arr)):
        sorted_arr.append(copy_arr.pop(find_smallest(copy_arr)))
    return sorted_arr

"""
3. Рекурсивная функция сумма чисел массива.
"""
def sum_recursive(arr: list) -> int:
    # Определим базовый случай
    if not arr:
        return 0
    return arr.pop() + sum_recursive(arr)

"""
4. Рекурсивная функция количество элементов массива.
"""
def count_recursive(arr: list) -> int:
    # Определим базовый случай
    if not arr:
        return 0
    return 1 + count_recursive(arr[1:])

"""
5. Рекурсивная функция для нахождения наибольшего числа в списке.
"""
def max_recursive(arr: list[int]) -> int:
    # Определим базовый случай
    if not arr:
        return 0
    x = max_recursive(arr[1:])
    if arr[0] > x:
        return arr[0]
    else:
        return x

"""
6. Бинарный поиск рекурсивный
"""
def binary_search_recursive(arr, item, min_idx=0, max_idx=None):
    if max_idx is None:
        max_idx = len(arr) - 1

    if min_idx <= max_idx:
        mid = min_idx + ((max_idx - min_idx) // 2)
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            return binary_search_recursive(arr, item, min_idx=min_idx, max_idx=mid - 1)
        else:
            return binary_search_recursive(arr, item, min_idx=mid + 1, max_idx=max_idx)
    else:
        return  None

# 1. Бинарный поиск (О(logN))
# print(binary_search([1, 3, 4, 7, 9], 4))
# print(binary_search([1, 3, 4, 7, 8, 10, 20, 39], 1))
# print(binary_search([1, 3, 4, 7, 9], 0))
# print(binary_search([1, 3, 4, 7, 9], 8))
# print(binary_search(['a', 'a', 'b', 'eee', 'ewq', 'q', 'w', 'zzz'], 'ewq'))

# 2. Сортировка выбором по возрастанию (O(N2))
# print(selection_sort([6, 8, 66, 899, 1, 0, 44, 356]))

# 3. Рекурсивная функция сумма чисел массива.
# print(sum_recursive([2, 4, 6]))

# 4. Рекурсивная функция количество элементов массива.
# print(count_recursive([2, 4, 6]))

# 5. Рекурсивная функция для нахождения наибольшего числа в списке.
# print(max_recursive([23, -44, 6]))

# 6. Бинарный поиск рекурсивный
print(binary_search_recursive([1, 3, 4, 7, 9], 4))
print(binary_search_recursive([1, 3, 4, 7, 8, 10, 20, 39], 1))
print(binary_search_recursive([1, 3, 4, 7, 9], 0))
print(binary_search_recursive([1, 3, 4, 7, 9], 8))
print(binary_search_recursive(['a', 'a', 'b', 'eee', 'ewq', 'q', 'w', 'zzz'], 'ewq'))