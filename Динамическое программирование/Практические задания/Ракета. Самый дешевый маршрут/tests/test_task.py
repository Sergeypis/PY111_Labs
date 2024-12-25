import unittest

from task import rocket_coasts


class TestCase(unittest.TestCase):
    def test_coast(self):
        coasts = [[2, 7, 9, 3], [12, 4, 1, 9], [1, 5, 2, 5]]
        expected_result = [[2, 9, 18, 21], [14, 13, 14, 23], [15, 18, 16, 21]]
        self.assertEqual(
            rocket_coasts(coasts), expected_result,
            msg="Таблица стоимостей рассчитана неверно :("
        )
