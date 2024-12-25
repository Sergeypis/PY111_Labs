import unittest

from task import stairway_path


class TestCase(unittest.TestCase):
    def test_some_stairs_coats(self):
        params = [
            # expected_value, stairs_coats
            (26, (1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3)),
            (19, (4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2)),
            (72, (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)),
            (41, (4, 12, 32, 22, 1, 7, 0, 12, 4, 2, 2))
        ]
        for expected_value, stairs_coats in params:
            with self.subTest(expected_value=expected_value, stairs_coats=stairs_coats):
                self.assertEqual(
                    expected_value, stairway_path(stairs_coats),
                    msg="Ожидаемый результат не сошелся с фактическим :("
                )

    def test_one_stair(self):
        stairs_coats = (10,)
        self.assertEqual(
            stairs_coats[0], stairway_path(stairs_coats),
            msg="Лестница с одной ступенью тоже лестница. Выбор не велик, просто наступаем на эту ступень"
        )

    def test_two_stairs(self):
        stairs_coats = (100000, 5)
        self.assertEqual(
            stairs_coats[1], stairway_path(stairs_coats),
            msg="Если ступеней всего две, то как ни крути дешевле наступить сразу на вторую"
        )
