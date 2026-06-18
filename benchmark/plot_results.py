import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv("benchmark/results.csv")

    plt.figure()
    plt.plot(data["nodes"], data["dijkstra_time"], marker="o", label="Dijkstra")
    plt.plot(data["nodes"], data["bellman_ford_time"], marker="o", label="Bellman-Ford")

    plt.xlabel("Number of Nodes")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Comparison: Dijkstra vs Bellman-Ford")
    plt.legend()
    plt.grid(True)

    plt.savefig("benchmark/runtime_plot.png")
    print("Plot saved to benchmark/runtime_plot.png")


if __name__ == "__main__":
    main()