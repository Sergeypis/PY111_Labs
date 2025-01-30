from math import trunc
from typing import Hashable, List, Set
import networkx as nx


def build_graph():
    edges_list = [
        ('A', 'C'),
        ('A', 'B'),
        ('C', 'F'),
        ('B', 'E'),
        ('B', 'D'),
        ('E', 'G')
    ]
    graph = nx.Graph()
    graph.add_edges_from(edges_list)
    return graph


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в глубину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    # реализовать обход в глубину

    path = []
    visited = {node: False for node in g.nodes}

    def dfs_recursive(current_node):
        path.append(current_node)
        visited[current_node] = True
        for neighbor in g[current_node]:
            if not visited[neighbor]:
                dfs_recursive(neighbor)
        return

    dfs_recursive(start_node)

    return path


if __name__ == '__main__':
    G = build_graph()
    print(dfs(G, 'A'))