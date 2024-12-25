import unittest

from task import calculate_paths


class TestCase(unittest.TestCase):
    def test_1(self):
        params = [  # expected_value, table_size
            (2, (4, 4)),
            (7884330, (15, 14)),
            (13309, (7, 15)),
            (1, (3, 2))
        ]
        for expected_value, table_size in params:
            with self.subTest(expected_value=expected_value, table_size=table_size):
                self.assertEqual(
                    expected_value, calculate_paths(table_size),
                    msg="Неверный расчет :("
                )
