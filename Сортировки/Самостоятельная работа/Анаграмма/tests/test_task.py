import unittest

from task import is_anagram


class TestIsAnagram(unittest.TestCase):

    def test_is_anagram(self):
        s = "anagram"
        t = "nagaram"
        result = is_anagram(s, t)
        self.assertTrue(result)

        s = "rat"
        t = "car"
        result = is_anagram(s, t)
        self.assertFalse(result)

        s = "a"
        t = "ab"
        result = is_anagram(s, t)
        self.assertFalse(result)
