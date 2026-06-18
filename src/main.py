import osmnx as ox
import folium
import heapq
import math
import time


def build_adjacency_list(G):
    graph = {}

    for node in G.nodes:
        graph[node] = []

    for u, v, data in G.edges(data=True):
        weight = data.get("length", 1)
        graph[u].append((v, weight))

    return graph


def dijkstra(graph, source, target):
    distance = {node: math.inf for node in graph}
    parent = {node: None for node in graph}
    visited = set()

    distance[source] = 0
    pq = [(0, source)]

    while pq:
        current_distance, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        if u == target:
            break

        for v, weight in graph[u]:
            new_distance = current_distance + weight

            if new_distance < distance[v]:
                distance[v] = new_distance
                parent[v] = u
                heapq.heappush(pq, (new_distance, v))

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return distance[target], path


def visualize_route(G, path, output_file="route_map.html"):
    route_coords = []

    for node in path:
        y = G.nodes[node]["y"]
        x = G.nodes[node]["x"]
        route_coords.append((y, x))

    center = route_coords[0]

    m = folium.Map(location=center, zoom_start=15)

    folium.Marker(
        route_coords[0],
        popup="Start",
        icon=folium.Icon(color="green")
    ).add_to(m)

    folium.Marker(
        route_coords[-1],
        popup="Destination",
        icon=folium.Icon(color="red")
    ).add_to(m)

    folium.PolyLine(
        route_coords,
        weight=5,
        opacity=0.8
    ).add_to(m)

    m.save(output_file)


place = "Surabaya, East Java, Indonesia"

G = ox.graph_from_place(
    place,
    network_type="drive",
    simplify=True
)

start_lat, start_lon = -7.2756, 112.7930
end_lat, end_lon = -7.2810, 112.7970

source = ox.distance.nearest_nodes(G, start_lon, start_lat)
target = ox.distance.nearest_nodes(G, end_lon, end_lat)

graph = build_adjacency_list(G)

start_time = time.perf_counter()
shortest_distance, path = dijkstra(graph, source, target)
end_time = time.perf_counter()

print("Shortest distance:", shortest_distance, "meters")
print("Runtime:", end_time - start_time, "seconds")
print("Path length:", len(path), "nodes")

visualize_route(G, path)