"""A script for the project in Algorithms Specialization (Stanford), course 3 (greedy algorithms) week 2
In the script both q1 and q2 are solved"""
import math
import unittest


class Unionfind:
    """Union-Find data structure for efficient union and find operations."""
    def __init__(self, size):
        """Initialize the Union-Find structure with specified size.

        Args:
            size (int): Number of elements in the union-find structure.
        """
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        """Find the root of the element x with path compression.

        Args:
            x (int): The element to find.

        Returns:
            int: The root of the element x.
        """
        if self.parent[x] !=x:
            self.parent[x] = self.find(self.parent[x]) #recursively call find on its parent
        return self.parent[x]

    def union(self, x, y):
        """Union the sets that contain elements x and y.

        Args:
            x (int): The first element.
            y (int): The second element.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] +=1

#Question 1:
def parse_file_q1(filename):
    """Parse the input file to create an adjacency list.

    Args:
        filename (str): Path to the input file.

    Returns:
        dict: Adjacency list representation of the graph, where keys are node ids
              and values are lists of tuples (neighbor, edge_cost).
    """
    adj_list = {}
    with open(filename, "r") as f:
        #skip number of nodes (first line)
        next(f)
        data = f.readlines()

    for line in data:
        line = line.rstrip().split()

        u = int(line[0])
        v = int(line[1])
        edge_cost = int(line[2])

        if u in adj_list:
            adj_list[u].append((v,edge_cost))

        else:
            adj_list[u] = [(v, edge_cost)]

        #the graph is complete so add the edge in reverse direction
        if v in adj_list:
            adj_list[v].append((u, edge_cost))
        else:
            adj_list[v] = [(u,edge_cost)]
    return adj_list


def merge_sort(edges):
    """Sort edges using merge sort.

    Args:
        edges (list): List of edges as tuples (node1, node2, cost).

    Returns:
        list: Sorted list of edges by cost in ascending order.
    """

    if len(edges) <= 1:
        return edges
    mid = len(edges) // 2
    left_half = merge_sort(edges[:mid])
    right_half = merge_sort(edges[mid:])

    return merge(left_half, right_half)


def merge(left, right):

    """Merge two sorted lists of edges into one sorted list.

    Args:
        left (list): First sorted list of edges.
        right (list): Second sorted list of edges.

    Returns:
        list: Merged sorted list of edges.
    """
    sorted_edges = []
    i = j = 0

    while i < len(left) and j <len(right):
        if left[i][2] <= right[j][2]:
            sorted_edges.append(left[i])
            i +=1
        else:
            sorted_edges.append(right[j])
            j +=1

    sorted_edges.extend(left[i:])
    sorted_edges.extend((right[j:]))

    return sorted_edges




def sort_edges(adj_List):
    """Extract and sort edges from the adjacency list.

    Args:
        adj_list (dict): Adjacency list representation of the graph.

    Returns:
        list: Sorted list of edges as tuples (node1, node2, cost).
    """
    edges = []
    for k, v in adj_List.items():
        for neighbor, cost in v :
            #avoid double counting edges
            if k < neighbor:
                edges.append((k,neighbor, cost))

    #perfrom selection sort in edges
    #sort_edges  = selection_sort(edges)

    #sort edges using merge_sort
    sorted_edges =  merge_sort(edges)
    return sorted_edges


def compute_distance(point1, point2):
    return math.dist(point1, point2)

def agglomerative_clustering(adj_list, num_clusters):
    """Perform agglomerative clustering using a union-find approach.

    Args:
        adj_list (dict): Adjacency list of the graph.
        num_clusters (int): Desired number of clusters.

    Returns:
        int: Maximum spacing of the clusters.
    """
    #sort the edges
    sorted_edges = sort_edges(adj_list)
    num_nodes = len(adj_list)

    #+1 for 1-indexed nodes
    uf = Unionfind(num_nodes +1)

    # Start with all nodes as separate clusters
    clusters = num_nodes
    #iterate through sorted list of edges
    for u,v, cost in sorted_edges:
        #check if u and v are in different clusters
        if uf.find(u) != uf.find(v):
            if clusters == num_clusters: # Desired number of clusters reached
                return cost
            # merge clusters
            uf.union(u,v)
            clusters -=1

    return None

#Question 2: Hierarchical clustering
def parseq2_to_ints(filename):
    """Parse input file for question 2 and convert binary strings to integers.

    Args:
        filename (str): Path to the input file.

    Returns:
        tuple: A tuple containing:
            - List of integers corresponding to binary strings.
            - Dictionary mapping integers to their indices.
    """
    with open(filename, "r") as f:
        #skip the first line
        next(f)
        data = f.readlines()

    nodes_to_ints = []
    #store int to the node indices
    ints_to_idx = {}
    for  idx, line  in enumerate(data):
        line = line.strip().replace(" ", "")

        #convert bit to int
        bit_to_int = int(line,2)
        nodes_to_ints.append(bit_to_int)

        # create a dic for mapping integers to their indeeces
        if bit_to_int not in ints_to_idx:
            ints_to_idx[bit_to_int] = {idx}
        else:
            ints_to_idx[bit_to_int].add(idx)

    return nodes_to_ints, ints_to_idx

import itertools
def generate_bitmasks(bits=24):
    """Generate bitmasks for Hamming distance of 1 and 2.

    Args:
        bits (int): Number of bits in the binary representation.

    Returns:
        list: List of generated bitmasks.
    """
    bitmasks = [0]  # Include the bitmask for Hamming distance 0
    print(bitmasks)
    #Genrate bitmask fo Hamming distance of 1.Left-wise bithift, each shift to the left multiplies the number by 2.
    for i in range(bits):
        print(1 << i)
        bitmasks.append(1 <<i)

    print(bitmasks)
    #Generate bitmasks of Hamming distance of 2
    for i, j in itertools.combinations(range(bits),2 ):
        bitmasks.append((1 << i) | (1 << j))
    print(bitmasks)
    return bitmasks


def largest_k_clustering_using_bitmasks(nodes_to_int,ints_to_idx,bits = 24):
    """Find the largest number of clusters using bitmasks for Hamming distance.

    Args:
        nodes_to_int (list): List of integers corresponding to the nodes.
        ints_to_idx (dict): Dictionary mapping integers to their indices.
        bits (int): Number of bits in the binary representation.

    Returns:
        int: The number of unique clusters.
    """
    len_nodes = len(nodes_to_int)
    uf = Unionfind(len_nodes)


    #generate bitmasks
    bitmasks = generate_bitmasks(bits)



    #itreerate over each unique integer
    for bit_value, node_ids in ints_to_idx.items():
        #try apply each bitmask (hamming distance of 0,1,2)
        for bitmask in bitmasks:
            neighbor_val = bit_value ^ bitmask


        #if the neighbor_val exists in the data perform union find
            if neighbor_val in ints_to_idx:
                for node_id in node_ids:
                    for neighbor_id in ints_to_idx[neighbor_val]:
                        uf.union(node_id, neighbor_id)


    #count the number of unique clusters
    clusters = len(set(uf.find(i) for i in range(len_nodes)))

    return clusters


def main():
    """Main function to run the clustering algorithms for both questions."""
    # Question 1
    adj_list_data = parse_file_q1("clustering1_q1.txt")
    num_clusters = 4
    max_spacing = agglomerative_clustering(adj_list_data, num_clusters)
    print(f'Maximum spacing for clustering: {max_spacing}')

    # Question 2
    nodes_to_int, ints_to_idx = parseq2_to_ints("clustering_big_q2.txt")
    largest_clusters = largest_k_clustering_using_bitmasks(nodes_to_int, ints_to_idx, bits=24)
    print(f'Largest clusters based on Hamming distance: {largest_clusters}')


if __name__ == "__main__":
    main()

