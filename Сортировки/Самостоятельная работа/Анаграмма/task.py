def is_anagram(s: str, t: str) -> bool:

    # return sorted(s) == sorted(t)

    if len(s) != len(t):
        return False

    dict_s: dict[str, int] = {}
    dict_t: dict[str, int] = {}

    for i in range(len(s)):
        if s[i] in dict_s:
            dict_s[s[i]] += 1
        else:
            dict_s[s[i]] = 1
        if t[i] in dict_t:
            dict_t[t[i]] += 1
        else:
            dict_t[t[i]] = 1
    return dict_s == dict_t