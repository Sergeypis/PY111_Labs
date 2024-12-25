from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dp = [[0] * n for _ in range(m)]
    ans = 0

    def dfs(i, j):
        # TODO реализовать поиск в глубину

    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))

    return ans
