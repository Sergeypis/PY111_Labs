from typing import Union, List

import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path_length
from networkx.algorithms.threshold import shortest_path


def build_graph(cost_node: tuple[int,...]) -> nx.DiGraph:
    def edges_list_generator():
        nodes_count = len(cost_node)
        a = iter(range(1, nodes_count))
        b = iter(range(0, nodes_count))
        i = 1
        while True:
            try:
                if not i % 2:
                    num_a = next(a)
                    yield num_a - 1, num_a + 1, cost_node[num_a]
                if i % 2:
                    num_b = next(b)
                    yield num_b, num_b + 1, cost_node[num_b]
                i += 1
            except StopIteration:
                return

    # weighted_edges_list: List[tuple[int, int, int]] = []
    # first_stage = (0, 1, cost_node[0])
    # weighted_edges_list.append(first_stage)
    #
    # for node in range(2, len(cost_node) + 1):
    #     weighted_edges_list.append((node - 2, node, cost_node[node - 1]))
    #     weighted_edges_list.append((node - 1, node, cost_node[node - 1]))

    # w = list(edges_list_generator())
    # print(w)

    g = nx.DiGraph()
    # g.add_weighted_edges_from(edges_list_generator())
    for a, b, cost in edges_list_generator():
        g.add_edge(a, b, cost=cost)

    return g


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы

    # nx.write_weighted_edgelist(graph, "edgelist")
    # paths = nx.single_source_dijkstra_path(graph, 0)
    lengths = nx.single_source_dijkstra_path_length(graph, 0, weight='cost')

    return lengths[max(lengths)]

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = build_graph(stairway) # записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
