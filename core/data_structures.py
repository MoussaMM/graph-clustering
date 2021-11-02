import pandas as pd
import networkx as nx
import numpy as np
from typing import Tuple

def to_nodes_dataframe(graph: nx.Graph)->pd.DataFrame:
    """Extract nodes info from a networkx graph and put it in a dataframe."""
    nodes_data = {"node_id": [], "position": [], "color": []}
    for node_id, graph_data in graph.nodes(data=True):
        nodes_data["node_id"].append(node_id)
        nodes_data["position"].append(graph_data["position"])
        nodes_data["color"].append(graph_data["color"])
    
    return pd.DataFrame(nodes_data)

def to_edges_dataframe(graph: nx.graph, nodes_dataframe: pd.DataFrame)-> pd.DataFrame:
    """Make edges dataframe from nodes dataframe and graph."""
    edges_data = {"node1": [], "node2": []}
    nodes_dataframe = nodes_dataframe[["node_id" ,"position"]]
    for node1, node2 in graph.edges(data=False):
        edges_data["node1"].append(node1)
        edges_data["node2"].append(node2)
    edges_data = pd.DataFrame(edges_data)
    edges_data = edges_data.merge(nodes_dataframe, how="left", left_on="node1", right_on="node_id")
    edges_data = edges_data.merge(nodes_dataframe, how="left", left_on="node2", right_on="node_id")
    import pdb; pdb.set_trace()
    edges_data["length"] = edges_data.apply(lambda x: np.sqrt(np.square(x.position_x[0]- x.position_y[0]) + np.square(x.position_x[1]- x.position_y[1])), axis=1)
    return edges_data[["node1", "node2", "length"]]

def to_dataframes(graph: nx.graph) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Make nodes and edges dataframes from graph."""
    nodes_dataframe = to_nodes_dataframe(graph)
    edges_dataframe = to_edges_dataframe(graph, nodes_dataframe)
    return nodes_dataframe, edges_dataframe

from core.create_graph import generate_random_graph
g = generate_random_graph(100, 500, ['red', 'blue'], 100, 100)
df1, df2 = to_dataframes(g)
import pdb; pdb.set_trace()
print('finally')