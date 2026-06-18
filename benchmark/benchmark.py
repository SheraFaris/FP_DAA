import os
import time
import csv
import random

from src.map_loader import load_road_graph
from src.graph_builder import build_adjacency_list
from src.dijkstra import dijkstra
from src.bellman_ford import bellman_ford

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_subgraph(original_graph, node_limit, seed=42):
    random.seed(seed)

    all_nodes = list(original_graph.nodes)

    if node_limit > len(all_nodes):
        node_limit = len(all_nodes)

    selected_nodes = random.sample(all_nodes, node_limit)
    subgraph = original_graph.subgraph(selected_nodes).copy()

    return subgraph


def get_valid_source_target(graph):
    nodes = list(graph.nodes)

    source = nodes[0]
    target = nodes[-1]

    return source, target


def run_benchmark():
    place_name = "Surabaya, East Java, Indonesia"
    sizes = [100, 300, 1000, 3000, 10000]
    seed = 42

    print("Loading full map...")
    full_graph = load_road_graph(place_name)

    with open("benchmark/results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "nodes",
            "edges",
            "dijkstra_time",
            "bellman_ford_time",
            "dijkstra_distance",
            "bellman_ford_distance",
            "same_result"
        ])

        for size in sizes:
            print(f"Benchmark size: {size}")

            subgraph = create_subgraph(full_graph, size, seed)
            graph = build_adjacency_list(subgraph)

            if len(graph) < 2:
                continue

            source, target = get_valid_source_target(subgraph)

            start = time.perf_counter()
            dijkstra_distance, _ = dijkstra(graph, source, target)
            dijkstra_time = time.perf_counter() - start

            start = time.perf_counter()
            bellman_distance, _ = bellman_ford(graph, source, target)
            bellman_time = time.perf_counter() - start

            same_result = round(dijkstra_distance, 2) == round(bellman_distance, 2)

            writer.writerow([
                len(subgraph.nodes),
                len(subgraph.edges),
                dijkstra_time,
                bellman_time,
                dijkstra_distance,
                bellman_distance,
                same_result
            ])

    print("Benchmark saved to benchmark/results.csv")


if __name__ == "__main__":
    run_benchmark()