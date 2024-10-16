import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(adj_list):
# Define the adjacency lis

    # Create a graph object
    graph = nx.Graph()


    # Add nodes and edges from the adjacency list
    for node, neighbors in adj_list.items():
        graph.add_node(node)
        for neighbor in neighbors:
            graph.add_edge(node, neighbor)

    # Draw the graph
    pos = nx.spring_layout(graph)  # Position nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title("Graph Visualization")
    plt.show()



