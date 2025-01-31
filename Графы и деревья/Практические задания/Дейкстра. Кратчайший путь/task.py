import math
import sys
from typing import Hashable, Mapping, Union
import networkx as nx


def build_graph():
    weighted_edges_list = [
        (1, 6, 14),
        (1, 2, 7),
        (1, 3, 9),
        (6, 3, 2),
        (6, 5, 9),
        (3, 6, 2),
        (3, 1, 9),
        (3, 2, 10),
        (3, 4, 11),
        (2, 1, 7),
        (2, 3, 10),
        (2, 4, 15),
        (4, 2, 15),
        (4, 3, 11),
        (4, 5, 6),
        (5, 4, 6),
        (5, 6, 9)
    ]

    g = nx.DiGraph()
    g.add_weighted_edges_from(weighted_edges_list)
    return g


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Функция с помощью алгоритма Дейкстры из модуля NetworkX находит кратчайшие пути до всех достижимых вершин графа.
    Если вершина не достижима, то стоимость пути до неё должна быть равно float("inf")

    :param g: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :param starting_node: Стартовый узел, откуда нужно начать обход
    :return: словарь как {'node1': 0, 'node2': 10, '3': 33, ...} со стоимостью путей, где node1, node2 - это узлы из графа g
    """
    # вернуть стоимость путей до всех вершин посчитанных алгоритмом Дейкстры

    def search_min_node():
        current_min_node = None
        for node in unvisited_nodes.keys():
            if current_min_node is None:
                current_min_node = node
            elif costs_path_list[node] < costs_path_list[current_min_node]:
                current_min_node = node
        return current_min_node


    costs_path_list = {node: sys.maxsize for node in g.nodes}
    costs_path_list[starting_node] = 0
    unvisited_nodes = {node: {} for node in g.nodes}

    while unvisited_nodes:
        min_node = search_min_node()
        neighbors = g[min_node]
        for nb in neighbors.keys():
            nb_new_weight = neighbors[nb].get('weight', 0) + costs_path_list[min_node]
            if costs_path_list[nb] > nb_new_weight:
                costs_path_list[nb] = nb_new_weight
        unvisited_nodes.pop(min_node)

    return costs_path_list


if __name__ == '__main__':
    # записать граф
    graph = build_graph()
    print(dijkstra_algo(graph, 1))  # {1: 0, 2: 7, 3: 9, 6: 11, 4: 20, 5: 20}
