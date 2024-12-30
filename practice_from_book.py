"""
1. Бинарный поиск
"""
def binary_search(arr, item):
    n = 0
    min_idx = 0
    max_idx = len(arr) - 1
    while min_idx <= max_idx:
        mid = (max_idx + min_idx)//2
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


# Бинарный поиск (О(logN))
# print(binary_search([1, 3, 4, 7, 9], 4))
# print(binary_search([1, 3, 4, 7, 6, 2, 0, 9], 1))
# print(binary_search([1, 3, 4, 7, 9], 0))
# print(binary_search([1, 3, 4, 7, 9], 8))
# print(binary_search(['qwe', 'a', 'asas', 'eee', 'ewq', 'q', 'w', 'e'], 'a'))

# Сортировка выбором по возрастанию (O(N2))
print(selection_sort([6, 8, 66, 899, 1, 0, 44, 356]))