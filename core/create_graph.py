import networkx as nx
from matplotlib.colors import is_color_like
import numpy as np
import matplotlib.pyplot as plt
from typing import List


def check_colors(color_list: List[str]):
    """Check that all colors are supported by matplotlib."""
    for color in color_list:
        assert is_color_like(
            color
        ), f"The color {color} is not supported by matplotlib!"


def generate_random_graph(
    number_of_points: int, number_of_edges: int, color_list: List[str], x_max: int, y_max: int
) -> nx.Graph:
    """Generate a random points graph."""
    point_positions = np.random.rand(number_of_points, 2)
    point_positions[:, 0] = point_positions[:, 0] * x_max
    point_positions[:, 1] = point_positions[:, 1] * y_max
    point_colors = np.random.choice(color_list, number_of_points)
    nodes_info = [
        (ind, {"color": point_color, "position": point_position})
        for ind, (point_position, point_color) in enumerate(
            zip(point_positions, point_colors)
        )
    ]
    edges = np.random.randint(number_of_points, size=(number_of_edges, 2))
    graph = nx.Graph()
    graph.add_nodes_from(nodes_info)
    graph.add_edges_from(edges)
    return graph


def draw_graph(graph: nx.Graph):
    """Draw a graph containing color and position data."""
    point_positions = {
        node_ind: node_data["position"]
        for node_ind, node_data in graph.nodes(data=True)
    }
    point_colors = [node_data["color"] for _, node_data in graph.nodes(data=True)]
    nx.draw(
        graph,
        pos=point_positions,
        node_color=point_colors,
        with_labels=True,
        font_color="white",
    )
    plt.show()
