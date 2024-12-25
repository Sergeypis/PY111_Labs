import unittest

from task import car_paths


class TestCase(unittest.TestCase):
    def test_coast(self):
        expected_result = [
            [1, 1, 1, 1, 1],
            [1, 3, 5, 7, 9],
            [1, 5, 13, 25, 41],
            [1, 7, 25, 63, 129],
            [1, 9, 41, 129, 321]
        ]
        self.assertEqual(
            car_paths(5, 5), expected_result,
            msg="Таблица путей рассчитана неверно :("
        )
