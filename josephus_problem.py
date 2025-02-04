def josephus(n, k):
    if n == 1:
        return 0
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result

# Пример использования
N = 90
K = 5
print(f"Номер последнего оставшегося человека: {josephus(N, K) + 1}")