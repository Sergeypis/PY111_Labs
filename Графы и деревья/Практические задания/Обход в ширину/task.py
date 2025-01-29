from typing import Hashable, List
from collections import deque

import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в ширину


if __name__ == '__main__':
    # записать граф с помощью модуля networkx и прверить обход в ширину

    node_list = {
        'A': ['B', 'F'],
        'B': ['A', 'G'],
        'F': ['A', 'G'],
        'G': ['B', 'F', 'I', 'H', 'C'],
        'I': ['H', 'G'],
        'H': ['I', 'D', 'E', 'J', 'C', 'G'],
        'C': ['H', 'G'],
        'J': ['H'],
        'E': ['H', 'D'],
        'D': ['E', 'H']
    }
    graph = nx.Graph()
    graph.add_nodes_from(node_list)
    print(graph.nodes)
    print(graph.edges)
