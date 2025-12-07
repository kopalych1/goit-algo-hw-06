from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def dfs(G: nx.Graph, start: int, to_find: int, visited=None):
    if visited is None:
        visited = set()

    if start in visited:
        return
    visited.add(start)

    if start == to_find:
        return start

    # print(start)

    for neighbor in G.neighbors(start):
        path = dfs(G, neighbor, to_find, visited)
        if isinstance(path, int):
            return [start, path]
        if isinstance(path, list):
            return [start] + path


def bfs(G: nx.Graph, start: int, to_find: int):
    visited = set([start])
    queue = deque([(start, [start], )])

    while queue:
        node, path = queue.popleft()

        if node == to_find:
            return path 

        # print(node)

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))


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
    print("BFS:", bfs(G, node_from, node_to))
    print("DFS:", dfs(G, node_from, node_to))

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
    test(G, 5, 9)
    test(G, 6, 5)

    display_graph(G)

if __name__ == "__main__":
    main()
