import heapq


def parse_graph(filename):
    """
    Parses a graph from a specified file and creates an adjacency list.

    Input:
        filename (str): The name of the file containing the graph data.
                        Each line contains two vertices and the cost of the edge between them.

    Output:
        dict: An adjacency list representing the graph, where each key is a vertex
              and its value is a list of tuples (neighbor, cost).
    """
    adj_list = {}
    with open(filename, 'r') as f:

        #skip first line
        #next(f)


        data = f.readlines()

        for line in data:
            line = line.rstrip().split()
            u = line[0]
            v = line[1]
            cost = int(line[2])

            if u in adj_list:
                adj_list[u].append((v, cost))
            else:
                adj_list[u] = [(v, cost)]

            # Add the edge in reverse direction for undirected graph
            if v in adj_list:
                adj_list[v].append((u, cost))
            else:
                adj_list[v] = [(u, cost)]
    return adj_list


def prims_algortihm(adj_list):
    """
    Implements Prim's algorithm to find the minimum spanning tree (MST) of a graph.

    Input:
        adj_list (dict): A graph represented as an adjacency list.

    Output:
        list: A list of tuples representing the edges of the MST,
              where each tuple is (node1, node2, weight).
    """

    #find total number of vertices
    total_vertices = len(adj_list)
    #start with an empty MSt
    mst = []
    included_vertices = set()
    min_cost = {v: float("Inf") for v in adj_list}
    parent = {v: None for v in adj_list}
    #start with an arbitrary vrtex
    start_vertex = next(iter(adj_list))
    min_cost[start_vertex] = 0
    print(min_cost)

    while len(included_vertices) < total_vertices:
        # Find the vertex with the minimum cost that is not included in the MST
        min_vertex = None
        for vertex in min_cost:
            if vertex not in included_vertices:
                if min_vertex is None or min_cost[vertex] < min_cost[min_vertex]:
                    min_vertex = vertex

        # Include this vertex in the MST
        included_vertices.add(min_vertex)

        # If the min_vertex has a parent, add the edge to MST
        if parent[min_vertex] is not None:
            print(f'this is the parent of min vertiex {parent[min_vertex]} with min_vertx {min_vertex}')
            mst.append((parent[min_vertex], min_vertex, min_cost[min_vertex]))

        # Explore all neighbors of min_vertex
        for neighbor, cost in adj_list[min_vertex]:
            if neighbor not in included_vertices and cost < min_cost[neighbor]:
                min_cost[neighbor] = cost
                parent[neighbor] = min_vertex
    return mst

def total_cost(mst):
    """
    Calculates the total cost of the minimum spanning tree (MST).

    Input:
        mst (list): The MST represented as a list of tuples,
                     where each tuple is (node1, node2, weight).

    Output:
        int: The total weight of the MST.
    """
    total_cost = 0
    for edge in mst:
        total_cost +=edge[2]

    return total_cost


def prim_heap(adj_list):
    """
    Implements Prim's algorithm using a priority queue (heap) for better performance.

    Input:
        adj_list (dict): A graph represented as an adjacency list.

    Output:
        list: A list of tuples representing the edges of the MST,
              where each tuple is (node1, node2, weight).
    """
    #a list to store edge of mst
    mst = []
    #a dic to keep track of min cost
    min_cost = {v: float('Inf') for v in adj_list}

    parent = {v: None for v in adj_list}

    included_vertices = set()

    #pick a start vertex
    start_vertex = next(iter(adj_list))
    min_cost[start_vertex] =0

    #min heap
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        #get the vertex with min cost
        cost, u = heapq.heappop(priority_queue)

        if u in included_vertices:
            continue

        included_vertices.add(u)

        if parent[u] is not None:
            mst.append([parent[u], u, cost])

        # Explore all neighbors of u
        for neighbor, cost in adj_list[u]:
            if neighbor not in mst and cost < min_cost[neighbor]:
                min_cost[neighbor] = cost
                parent[neighbor] = u
                heapq.heappush(priority_queue, (cost, neighbor))


    return mst

def main():
    adj_list = parse_graph('test.txt')

    mst = prims_algortihm(adj_list)
    total_mst_cost = total_cost(mst)
    print(f'This is the total cost of mst {total_mst_cost}')

    # Compute the MST using Prim's algorithm with a heap for improved performance
    mst_heap = prim_heap(adj_list)
    print(mst_heap)

if __name__ == '__main__':
    main()