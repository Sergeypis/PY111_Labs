def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    # написать итеративный алгоритм чисел Фибоначчи

    if n < 0:
        raise ValueError("Ошибка. Должно быть не отрицательное число.")
    if n == 0:
        return 0
    first = 0
    second = 1
    for _ in range(n - 1):
        first, second = second, first + second

    return second
