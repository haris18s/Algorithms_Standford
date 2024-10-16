#! usr/bin/env python3

import heapq


def parse_data(file):
    adj_list_gr = {}
    with open(file, "r") as f:
        data = f.readlines()



    for line in data:
        line = line.split()
        if line == []:
            continue
        vertex = int(line[0])
        edges = [(int(neighbor.split(",")[0]), int(neighbor.split(",")[1])) for neighbor in line[1:]]
        adj_list_gr[vertex] = edges
    return adj_list_gr


def dijkstra(graph,source_vertex):

    """dijkstra algorithm to find shortest path for each vertex
    Inputs:
        - graph: A dictionary representing the graph as an adjacency list.
        - source_vertex: The starting vertex for the algorithm.
    Outputs:
     - predecessors: A dictionary showing the vertex immediately before each vertex on the shortest path.
    - distances: A dictionary with the minimum distance from the source to each vertex.

    """
    #initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[source_vertex] = 0
    unvisited = set(graph.keys())

    predecessors = {}

    while unvisited:
        #find the vertex with min distanc in the unvisited set
        current_vertex = None
        for vertex in unvisited:
            if current_vertex is None or distances[vertex]  < distances[current_vertex]:
                current_vertex  = vertex


        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, length in graph[current_vertex]:
            distance_to_curr_vertex = distances[current_vertex] + length

            if distance_to_curr_vertex < distances[neighbor]:
                distances[neighbor] = distance_to_curr_vertex
                predecessors[neighbor] = current_vertex

        unvisited.remove(current_vertex)
    return predecessors, distances




def dijkstra_minheap(graph, source_vertex):
    """
        Optimized version of Dijkstra's algorithm using a min-heap (priority queue).
        Inputs:
        - graph: A dictionary representing the graph as an adjacency list.
        - source_vertex: The starting vertex for the algorithm.

        Outputs:
        - predecessors: A dictionary showing the vertex immediately before each vertex on the shortest path.
        - distances: A dictionary with the minimum distance from the source to each vertex.
        """
    distances = {vertex : float('inf') for vertex in graph}
    distances[source_vertex] = 0

    #initializ predec
    predecessors = {}
    heap = [(0, source_vertex)]
    visited = set()

    while heap:
        #extract the vertex with min distance
        curr_distance, curr_vertex = heapq.heappop(heap)

        if curr_vertex in visited:
            continue
        visited.add(curr_vertex)

        for neighbor,length in graph[curr_vertex]:
            distance = curr_distance + length

            #if there is a shorted path to the neighbor
            if distances[curr_vertex] <distances[neighbor]:
                distances[neighbor]  = distance
                predecessors[neighbor] = curr_vertex
                heapq.heappush(heap, (distance, neighbor))

    return predecessors, distances



def reconstruct_path(predecessors, start_vertex, end_vertex):
    """
    Reconstructs the shortest path from the start vertex to the end vertex using the predecessors dictionary.
    Inputs:
    - predecessors: A dictionary mapping each vertex to the vertex that precedes it on the shortest path.
    - start_vertex: The vertex from which the path starts.
    - end_vertex: The vertex to which the path is being reconstructed.

    Output:
    - A list representing the shortest path from start_vertex to end_vertex.
    """
    path = []
    current_vertex = end_vertex
    while current_vertex != start_vertex:
        path.append(current_vertex)
        current_vertex = predecessors.get(current_vertex)

        if current_vertex is None:
            return []
    path.append(start_vertex)
    path.reverse()
    return path

def print_path(graph, predecessors):
    """
    Prints the shortest paths from the start vertex to all other vertices in the graph.
    Inputs:
    - graph: The graph as an adjacency list.
    - predecessors: The dictionary showing the predecessors of each vertex.
    """
    for vertex in sorted(graph.keys()):
        path = reconstruct_path(predecessors, 1, vertex)
        #exlude start vertex from itws own path display
        path_to_display = path[1:] if path else []
        print(f"{vertex} {distances[vertex]} {path_to_display}")


if __name__ == "__main__":

    #Parse input to create the adj list
    graph = parse_data("test.txt")

    predecessors,distances = dijkstra(graph, 1)

    print_path(graph, predecessors)

    #using min heap
    predecessors1,distances1 = dijkstra_minheap(graph, 1)

    print_path(graph, predecessors1)

