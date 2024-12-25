import unittest

from task import replace_words


class TestSolution(unittest.TestCase):
    def test_replaceWords(self):
        self.assertEqual(replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery"), "the cat was rat by the bat")
        self.assertEqual(replace_words(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"), "a a a a a a a a bbb baba a")
