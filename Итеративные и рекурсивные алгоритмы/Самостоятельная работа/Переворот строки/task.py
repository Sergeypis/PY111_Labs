from typing import List


def reverse_string(s: List[str]) -> None:

    # list_ = []
    # for _ in range(len(s)):
    #     list_.append(s.pop())
    # print(list_)

    # s = s[::-1]
    # print(s)

    # s.reverse()
    # print(s)

    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    print(s)

reverse_string(['h', 'e', 'l', 'l', 'o'])