import unittest

import networkx as nx

from task import dfs


class TestCase(unittest.TestCase):
    def test_dfs(self):
        graph = nx.Graph()
        graph.add_nodes_from("ABCDEFG")
        graph.add_edges_from([
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'D'),
            ('B', 'E'),
            ('C', 'F'),
            ('E', 'G'),
        ])
        result = dfs(graph, 'A')
        self.assertEqual(
            7,
            len(result),
            msg="Проверьте возвращаемый список - в него либо затесались лишние элементы, либо не хватает элементов."
        )

        self.assertIn(
            result,
            [
                list('ABDEGCF'),
                list('ABEGDCF'),
                list('ACFBDEG'),
                list('ACFBEGD')
            ],
            msg="Возвращаемый список несоответствует нужному порядку обхода."
        )
