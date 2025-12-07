import heapq

import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(G: nx.Graph, start: int, to_find: int) -> list[int]:
    dist = {v: float('inf') for v in G.nodes}
    dist[start] = 0

    parent = {v: None for v in G.nodes}

    pq = [(0, start)]  # (dist, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        if u == to_find:
            break

        for v in G.neighbors(u):
            w = G[u][v].get("weight", 1)
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    path = []
    cur = to_find
    if dist[cur] == float('inf'):
        return []

    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    return path[::-1]


def display_graph(G: nx.Graph) -> None:
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=1500, font_size=16, font_weight='bold',
            edge_color='gray', width=2)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Simple graph", fontsize=14)
    plt.show()


def test(G: nx.Graph, node_from: int, node_to: int):
    print(f"Path from {node_from} -> {node_to}")
    print(dijkstra(G, node_from, node_to))


def main():
    G = nx.Graph()

    nodes = list(range(1, 10))

    G.add_nodes_from(nodes)
    G.add_weighted_edges_from([
        (1, 2, 1),
        (1, 3, 4),
        (2, 3, 5),
        (3, 4, 6),
        (4, 5, 2),
        (4, 2, 9),
        (1, 6, 1),
        (6, 7, 4),
        (6, 8, 2),
        (5, 8, 7),
        (6, 9, 6)
    ])

    test(G, 1, 8)
    test(G, 1, 5)
    test(G, 2, 8)

    display_graph(G)

if __name__ == "__main__":
    main()
