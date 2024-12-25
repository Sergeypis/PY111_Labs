import unittest

import networkx as nx

from task import stairway_path


class TestCase(unittest.TestCase):
    def test_some_stairs_coats(self):
        # params = [
        #     # expected_value, stairs_coats
        #     (19, (4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2)),
        #     (41, (4, 12, 32, 22, 1, 7, 0, 12, 4, 2, 2))
        # ]
        params = [
            ([
                (0, 1, 1),
                (0, 2, 3),
                (1, 2, 3),
                (1, 3, 1),
                (2, 3, 1),
                (2, 4, 5),
                (3, 4, 5),
                (3, 5, 2),
                (4, 5, 2),
                (4, 6, 7),
                (5, 6, 7),
                (5, 7, 7),
                (6, 7, 7),
                (6, 8, 8),
                (7, 8, 8),
                (7, 9, 9),
                (8, 9, 9),
                (8, 10, 4),
                (9, 10, 4),
                (9, 11, 6),
                (10, 11, 6),
                (10, 12, 3),
                (11, 12, 3),
            ], (1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3), 26),
            ([
                 (0, 1, 4),
                 (0, 2, 4),
                 (1, 2, 4),
                 (1, 3, 3),
                 (2, 3, 3),
                 (2, 4, 2),
                 (3, 4, 2),
                 (3, 5, 3),
                 (4, 5, 3),
                 (4, 6, 4),
                 (5, 6, 4),
                 (5, 7, 5),
                 (6, 7, 5),
                 (6, 8, 9),
                 (7, 8, 9),
                 (7, 9, 1),
                 (8, 9, 1),
                 (8, 10, 2),
                 (9, 10, 2),
                 (9, 11, 4),
                 (10, 11, 4),
                 (10, 12, 2),
                 (11, 12, 2),
            ], (4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2), 19),
        ]

        for list_edges, stairway, expected_value in params:
            with self.subTest(expected_value=expected_value, stairway=stairway):
                graph = nx.DiGraph()
                graph.add_weighted_edges_from(list_edges)
                self.assertEqual(
                    expected_value, stairway_path(graph),
                    msg="Ожидаемый результат не сошелся с фактическим :("
                )

    # def test_one_stair(self):
    #     stairs_coats = (10,)
    #     self.assertEqual(
    #         stairs_coats[0], stairway_path(stairs_coats),
    #         msg="Лестница с одной ступенью тоже лестница. Выбор не велик, просто наступаем на эту ступень"
    #     )
    #
    # def test_two_stairs(self):
    #     stairs_coats = (100000, 5)
    #     self.assertEqual(
    #         stairs_coats[1], stairway_path(stairs_coats),
    #         msg="Если ступеней всего две, то как ни крути дешевле наступить сразу на вторую"
    #     )
