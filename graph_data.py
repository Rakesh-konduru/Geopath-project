import networkx as nx

G = nx.Graph()

G.add_weighted_edges_from([
    ("Airport", "MG Road", 10),
    ("Airport", "Whitefield", 5),
    ("Whitefield", "Indiranagar", 3),
    ("MG Road", "Indiranagar", 8),
    ("Whitefield", "Electronic City", 6),
    ("Electronic City", "Koramangala", 4),
    ("Koramangala", "MG Road", 7)
])