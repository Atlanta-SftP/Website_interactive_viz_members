import networkx as nx
from networkx.readwrite import json_graph
import pandas as pd
from matplotlib.pylab import plt
 
G = nx.Graph()
 
# Read csv for nodes and edges using pandas:
nodes = pd.read_csv("nodes.csv")
edges = pd.read_csv("edges.csv")
 
# Dataframe to list:
nodes_list = nodes.values.tolist()
print nodes_list
edges_list = edges.values.tolist()
print edges_list
 
# Import id, name, and group into node of Networkx:
for i in nodes_list:
    G.add_node(i[0], name=i[1], type=i[2],img=i[3],size=i[4])
 
# Import source, target, and value into edges of Networkx:
for i in edges_list:
    G.add_edge(i[0],i[1])
 
# Visualize the network:
#nx.draw_networkx(G)

# Write json for nodes-links format:
import json
j = json_graph.node_link_data(G)
 
js = json.dumps(j, ensure_ascii=False, indent=2)
with open("node-link-value.json", "w") as file:
     file.write(js)