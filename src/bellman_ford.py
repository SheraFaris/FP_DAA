import math


def bellman_ford(graph, source, target):
    """
    Implementasi Bellman-Ford dari awal.
    Digunakan sebagai pembanding untuk Dijkstra.
    """

    distance = {}
    parent = {}

    for node in graph:
        distance[node] = math.inf
        parent[node] = None

    distance[source] = 0

    edges = []

    for u in graph:
        for v, weight in graph[u]:
            edges.append((u, v, weight))

    vertex_count = len(graph)

    for _ in range(vertex_count - 1):
        updated = False

        for u, v, weight in edges:
            if distance[u] != math.inf and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
                updated = True

        if not updated:
            break

    for u, v, weight in edges:
        if distance[u] != math.inf and distance[u] + weight < distance[v]:
            raise ValueError("Graph contains a negative weight cycle")

    path = reconstruct_path(parent, source, target)

    return distance[target], path


def reconstruct_path(parent, source, target):
    path = []
    current = target

    while current is not None:
        path.append(current)

        if current == source:
            break

        current = parent[current]

    path.reverse()

    if not path or path[0] != source:
        return []

    return path