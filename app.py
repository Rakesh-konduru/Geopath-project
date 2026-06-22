from flask import Flask, render_template, request
import networkx as nx
from graph_data import G
from graph_visualizer import draw_graph
from flask import jsonify
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    shortest_path = None
    total_distance = None

    # Draw initial graph when page loads
    draw_graph(G)

    if request.method == "POST":

        source = request.form["source"]
        destination = request.form["destination"]

        try:
            shortest_path = nx.dijkstra_path(
                G,
                source,
                destination,
                weight="weight"
            )

            total_distance = nx.dijkstra_path_length(
                G,
                source,
                destination,
                weight="weight"
            )

            # Highlight shortest path in red
            draw_graph(G, shortest_path)
            print("draw_graph called..!")

        except nx.NetworkXNoPath:
            shortest_path = ["No path found"]
            total_distance = None

    areas = list(G.nodes())

    return render_template(
        "index.html",
        areas=areas,
        shortest_path=shortest_path,
        total_distance=total_distance
    )



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    