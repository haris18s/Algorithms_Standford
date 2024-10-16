#! usr/bin/env python3

"""Kosaraju algorithm in order to find the size of the largest Strongly connected components (SCCs) of a graph"""

#Import my function to visualize the graph
import sys
from Visualize_a_Graph import visualize_graph
sys.setrecursionlimit(10000000)


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
    """Performs a Depth-First Search (DFS) traversal on a graph recursively.

    Input:
    - graph (dict): The graph represented as a dictionary.
    - node: The current node being visited during the DFS traversal.
    - visited_nodes (set): A set to keep track of nodes that have been visited.
    - finishing_times (list): A list to store the finishing times of nodes in the DFS traversal.
    """

    #initialize a stack to keep track nodes
    if node not  in visited_nodes:
        visited_nodes.add(node)
        for neighbor in graph[node]:
            DFFS_recursive(graph, neighbor, visited_nodes, finishing_times)
        finishing_times.append(node)

def DFS_iterative(graph, node, visited_nodes, scc):
    """Performs an iterative DFS to find a strongly connected component.

    Input:
    - graph (dict): The graph represented as a dictionary.
    - node: The starting node for the DFS.
    - visited_nodes (set): A set to keep track of visited nodes.
    - scc (list): A list to store the nodes in the current strongly connected component.
    """
    stack = [node]
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited_nodes:
            visited_nodes.add(curr_node)
            scc.append(curr_node)
            for neighbor in graph[curr_node]:
                if neighbor not in visited_nodes:
                    stack.append(neighbor)

        else:
            scc.append(node)


def kosaraju(adj_list):
    """Finds the strongly connected components (SCCs) of the graph using Kosaraju's algorithm.

    Input: Adjacency list (dict).
    Output: List of SCCs, where each SCC is a list of nodes.
    """
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
            DFS_iterative(reversed_graph, node, visited_nodes, scc)
            sccs.append(scc)

    return sccs



def largest5_sccs(sccs):
    """Calculates the 5 largest SCCs from a list of SCCs.

    Input: sccs (list of list) with each element being a component of SCC.
    Output: The largest 5 components in descending order.
    """
    largest_sccs = sorted(sccs, key = len, reverse = True)

    len_largest_scc = [len(scc) for scc in largest_sccs[:5]]
    #output without spaces for answer
    largest_sccs_formatted  = ",".join(str(scc) for scc in len_largest_scc)

    return largest_sccs_formatted

def main():
    #Parse the input data
    data = parse_input('SCC_input_file')
    #visualize graph
    #visualize_graph(data)
    #find the SCCs
    sccs = kosaraju(data)

    #Print the largest SCCs
    top5 = largest5_sccs(sccs)
    print(top5)

if __name__ == "__main__":

    main()