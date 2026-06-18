import heapq
import math


def dijkstra(graph, source, target):
    """
    Implementasi Dijkstra dari awal menggunakan priority queue.
    Tidak memakai fungsi shortest path dari library.
    """

    distance = {}
    parent = {}
    visited = set()

    for node in graph:
        distance[node] = math.inf
        parent[node] = None

    distance[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == target:
            break

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

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