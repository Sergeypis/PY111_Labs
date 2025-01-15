from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # реализовать алгоритм сортировки пузырьком

    x = 0
    change_flag = True
    while x < len(container) - 1 and change_flag:
        change_flag = False
        for idx in range(len(container) - 1 - x):
            val_1 = container[idx]
            val_2 = container[idx + 1]
            if val_1 > val_2:
                container[idx], container[idx + 1] = val_2, val_1
                change_flag = True
        x += 1
    return container


print(sort([6,5,3,1,8,7,2,4]))