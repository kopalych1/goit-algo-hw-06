import networkx as nx
import matplotlib.pyplot as plt


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

    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())
    print("Degrees:", [G.degree(node) for node in nodes])

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1500, font_size=16, font_weight='bold',
            edge_color='gray', width=2)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Simple graph", fontsize=14)
    plt.show()

if __name__ == "__main__":
    main()
