def build_adjacency_list(osmnx_graph):
    """
    Mengubah graph dari OSMnx menjadi adjacency list sederhana.

    Format:
    graph[u] = [(v, weight), (v2, weight2), ...]
    """

    graph = {}

    for node in osmnx_graph.nodes:
        graph[node] = []

    for u, v, data in osmnx_graph.edges(data=True):
        weight = data.get("length", 1)
        graph[u].append((v, weight))

    return graph