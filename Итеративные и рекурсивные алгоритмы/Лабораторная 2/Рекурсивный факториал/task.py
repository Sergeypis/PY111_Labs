def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # реализовать рекурсивный алгоритм нахождения факториала
    if not isinstance(n, int):
        raise TypeError("Error! Number n must be is integer.")
    if n < 0:
        raise ValueError("Error! Number n must be positive.")
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n