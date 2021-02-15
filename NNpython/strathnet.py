import networkx as nx
import matplotlib.pyplot as plt
from classes.greedybfs import GreedyBFS

G = nx.Graph()
nodes = ["Sport_complex", "siwaka", "ph1A", "ph1B", "phase2", "J1", "Mada", "STC", "Phase3", "Parking-Lot"]
G.add_nodes_from(nodes)
G.add_edge("Sport_complex", "siwaka", weight="450")
G.add_edge("siwaka", "ph1A", weight="10")
G.add_edge("siwaka", "ph1B", weight="230")
G.add_edge("ph1A", "ph1B", weight="100")
G.add_edge("ph1A", "Mada", weight="850")
G.add_edge("ph1B", "phase2", weight="112")
G.add_edge("phase2", "J1", weight="600")
G.add_edge("phase2", "Phase3", weight="500")
G.add_edge("phase2", "STC", weight="50")
G.add_edge("Phase3", "Parking-Lot", weight="350")
G.add_edge("J1", "Mada", weight="200")
G.add_edge("Mada", "Parking-Lot", weight="700")
G.add_edge("STC", "Parking-Lot", weight="250")

G.nodes["Sport_complex"]['pos'] = (-4, 4)
G.nodes["siwaka"]['pos'] = (-2, 4)
G.nodes["ph1A"]['pos'] = (0, 2)
G.nodes["ph1B"]['pos'] = (0, 0)
G.nodes["phase2"]['pos'] = (2, 0)
G.nodes["J1"]['pos'] = (4, 0)
G.nodes["Mada"]['pos'] = (7, 0)
G.nodes["STC"]['pos'] = (0, -2)
G.nodes["Phase3"]['pos'] = (4, -3)
G.nodes["Parking-Lot"]['pos'] = (4, -6)

# storing all positions inside a variable
node_pos = nx.get_node_attributes(G, 'pos')
pos=nx.spring_layout(G)
# call BFS class
route_by_BFS = GreedyBFS()
routes = route_by_BFS.gbfs(G, "Sport_complex", "Parking-Lot")
print(route_by_BFS.visited)
route_list = route_by_BFS.visited
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list, route_list[1:]))
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col)
# nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
