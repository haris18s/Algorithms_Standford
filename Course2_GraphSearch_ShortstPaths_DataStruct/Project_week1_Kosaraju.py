"""Kosaraju algorithm in order to find the size of the largest Strongly connected components (SCCs) of a graph"""

#Import my function to visualize the graph
import sys

def parse_input(input_file):
    """Function to parse the input file into adj_list
    Input:: txt file wih the vertex label in first column is the tail and the vertex label in second column is the head.

    Outputs: adj_list as a dic, with key as the vertex and the value as a list with its neighbors
    """
    with open(f"{input_file}.txt") as file:
        data = file.readlines()
    adj_list = {}
    for line in data:
        line = line.strip()
        if line:
            vertex, neighbor = map(int, line.split())
            adj_list.setdefault(vertex,[]).append(neighbor)
            adj_list.setdefault(neighbor, [])
    return adj_list



def reverse_graph(adj_list):
    """This function reverse the graph in order to be used for Kosaraju algorithm

    Input: Adjacency list represented a s a dic
    Output: Reversed graph in form of adj.list

    """
    reversed_adj_list = {node: [] for node in adj_list.keys()}
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            reversed_adj_list.setdefault(neighbor, []).append(node)
    return reversed_adj_list

def DFFS_recursive(graph, node, visited_nodes, finishing_times):
    """DFS recursive: This function performs a Depth-First Search (DFS) traversal on a graph recursively
    It better use the DFS_iterative method for large input, because there is an rcersion limit.

     Input:
     graph (dict): The graph represented as a dictionary where keys are nodes and values are lists of neighboring nodes.
        node: The current node being visited during the DFS traversal.
        visited_nodes (set): A set to keep track of nodes that have been visited to avoid revisiting them.
        finishing_times (list): A list to store the finishing times of nodes in the DFS traversal
     """

    #initialize a stack to keep track nodes
    if node not  in visited_nodes:
        visited_nodes.add(node)
        for neighbor in graph[node]:
            DFFS_recursive(graph, neighbor, visited_nodes, finishing_times)
        finishing_times.append(node)

def DFS_iterative(graph, node, visited_nodes, finishing_times):

    stack = [node]
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited_nodes:
            visited_nodes.add(curr_node)
            for neighbor in graph[curr_node]:
                if neighbor not in visited_nodes:
                    stack.append(neighbor)
        else:
            finishing_times.pop(curr_node)




def kosaraju(adj_list):
    # Step 1: Reverse the graph
    reversed_graph = reverse_graph(adj_list)

    # Step 2: First DFS pass to compute finishing times
    visited_nodes = set()
    finishing_times = []
    for node in adj_list:
        if node not in visited_nodes:
            DFFS_recursive(adj_list, node, visited_nodes, finishing_times)

    # Reset visited nodes for the second DFS pass
    visited_nodes.clear()
    sccs = []

    # Step 3: Second DFS pass to identify SCCs
    for node in reversed(finishing_times):
        if node not in visited_nodes:
            scc = []
            DFFS_recursive(reversed_graph, node, visited_nodes, scc)
            sccs.append(scc)

    return sccs



def largest5_sccs(sccs):
    """Calculates that  5 largest sccs from a list of lists with Sccs

    Input: sccs(list of list) with each element been a component of scc
    Output: the largest 5 components in decrestion order

    """
    largest_sccs = sorted(sccs, key = len, reverse = True)

    len_largest_scc = [len(scc) for scc in largest_sccs[:5]]
    #output without spaces for answer
    largest_sccs_formatted  = ",".join(str(scc) for scc in len_largest_scc)

    return largest_sccs_formatted



if __name__ == "__main__":

    #Parse the input data
    data = parse_input('test_case')

    #find the SCCs
    sccs = kosaraju(data)

    #Print the largest SCCs
    top5 = largest5_sccs(sccs)
    print(top5)









