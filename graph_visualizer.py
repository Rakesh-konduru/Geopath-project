import os
import matplotlib
matplotlib.use('Agg')  # IMPORTANT for Render
import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(G, path=None):

    plt.figure(figsize=(8, 6))

    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=500)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color="gray")

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight shortest path if exists
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

    # 🔥 FIX FOR RENDER (absolute path)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")

    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    file_path = os.path.join(static_dir, "route.png")

    print("Saving image at:", file_path)

    plt.savefig(file_path)
    plt.close()
