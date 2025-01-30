from typing import Hashable, List
import matplotlib.pyplot as plt
from bokeh.palettes import Spectral
from collections import deque

import networkx as nx
from networkx.classes import nodes, all_neighbors


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    # реализовать обход в ширину

    nodes_list: List[Hashable] = []
    visit_queue = deque()
    queue_cache = set()

    visit_queue.append(start_node)
    queue_cache.add(start_node)

    while visit_queue:
        node = visit_queue.popleft()
        nodes_list.append(node)

        for nb in all_neighbors(g, node):
            if nb not in queue_cache:
                visit_queue.append(nb)
                queue_cache.add(nb)

    return nodes_list

    # visited = {node: False for node in g.nodes}
    # d = deque()  # начало слева, конец справа
    # path = []
    #
    # d.append(start_node)  # поджигаем узел графа
    # visited[start_node] = True  # если узел "подожжен", то мы его посещали
    # while d:
    #     current_node = d.popleft()
    #     path.append(current_node)
    #     for neighbor in g[current_node]:  # g[current_node] - смежные узлы
    #         if not visited[neighbor]:
    #             d.append(neighbor)  # поджигаем узел графа
    #             visited[neighbor] = True  # если узел "подожжен", то мы его посещали
    #
    # return path


if __name__ == '__main__':
    # записать граф с помощью модуля networkx и прверить обход в ширину

    adjacency_list = {
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

    edges_list = [
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('H', 'I'),
        ('H', 'J'),
        ('H', 'E'),
        ('H', 'D'),
        ('E', 'D')
    ]

    plt.figure(figsize=(8, 8))  # Размер поля для вывода
    graph = nx.Graph()
    graph.add_edges_from(edges_list)
    pos = nx.spring_layout(graph)  # Шаблон вывода графа
    options = {  # Опции отрисовки
        # 'node_color': 'yellow',
        'node_color': Spectral[10],
        'node_size': 600,
        'width': 1,
        # 'arrowstyle': '-|>',
        # 'arrowsize': 18,
        'edge_color': 'blue',
    }
    # print(graph.nodes)
    # print(graph.edges)
    nx.draw_networkx(
        G=graph,
        pos=pos,
        # arrows=True
        with_labels=True,
        **options
    )

    ax = plt.gca()  # Очерчивание узлов
    ax.collections[0].set_edgecolor("#000000")

    print(bfs(graph, 'A'))
