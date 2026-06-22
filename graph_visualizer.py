import networkx as nx
import matplotlib.pyplot as plt
import os
print("graph_visualizer loaded")

def draw_graph(G, shortest_path=None):
    print("Inside draw_graph")
    plt.figure(figsize=(10, 8))

    pos = nx.spring_layout(G, seed=42)

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color="skyblue",
        node_size=2500
    )

    # Draw edges
    nx.draw_networkx_edges(
        G,
        pos,
        width=2
    )

    # Draw labels
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=10
    )

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels
    )

    # Highlight shortest path
    if shortest_path:
        path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            edge_color="red",
            width=5
        )

    plt.axis("off")
    plt.tight_layout()

    print("Saving image...")
    static_path = os.path.join("static", "route.png")
    plt.savefig(static_path)
    print("Image saved!")

    plt.close()