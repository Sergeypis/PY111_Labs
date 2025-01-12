def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # реализовать итеративный алгоритм нахождения факториала

    if n < 0:
        raise ValueError("Error! Number n must be positive.")
    if n <= 1:
        return 1
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result

print(factorial_iterative(1))