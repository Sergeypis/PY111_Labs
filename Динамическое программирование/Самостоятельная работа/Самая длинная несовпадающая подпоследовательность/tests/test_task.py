import unittest

from task import find_lus_length


class TestLongestUncommonSubsequenceII(unittest.TestCase):
    def test_longest_uncommon_subsequence_ii(self):
        strs = ["aaa", "bbb", "ccc"]
        longest_uncommon_length = find_lus_length(strs)
        self.assertEqual(longest_uncommon_length, 3)

        strs = ["aabbcc", "aabbcc", "cb", "cac"]
        longest_uncommon_length = find_lus_length(strs)
        self.assertEqual(longest_uncommon_length, 3)

        strs = ["aabbcc", "aabbcc", "cb"]
        longest_uncommon_length = find_lus_length(strs)
        self.assertEqual(longest_uncommon_length, 2)

        strs = ["aabbcc", "aabbcc"]
        longest_uncommon_length = find_lus_length(strs)
        self.assertEqual(longest_uncommon_length, -1)
