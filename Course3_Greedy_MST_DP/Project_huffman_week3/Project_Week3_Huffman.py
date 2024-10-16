import heapq

def parse_data_q1(filename):
    """Parse weights from a file.

    Args:
        filename (str): Path to the input file containing weights.

    Returns:
        list: A list of integer weights (frequencies of symbols).
    """

    with open(filename) as f:
        #skip the number of symbols
        next(f)
        data = f.readlines()

    lis_weights = [int(line.strip()) for line in data]

    return lis_weights

def huffman_implem(lis_weights):
    """Compute the maximum and minimum lengths of codewords in a Huffman code.

    Args:
        lis_weights (list): A list of weights (frequencies of symbols).

    Returns:
        tuple: (max_depth, min_depth) where:
            - max_depth (int): Maximum depth (length of the longest codeword).
            - min_depth (int): Minimum depth (length of the shortest codeword).
    """
    # Initialize the heap with tuples of (weight, max depth, min depth)

    heap_data = [(weight,0,0) for weight in lis_weights]
    heapq.heapify(heap_data)

    max_depth = 0
    min_depth = float("inf")  # Initialize min_depth to infinity


    while len(heap_data) >1:
        # Pop the two nodes with the smallest weights
        left_node = heapq.heappop(heap_data)
        right_node = heapq.heappop(heap_data)
        merged_freq = left_node[0] + right_node[0]

        # Determine the max and min depths after merging
        merged_depth_max = max(left_node[1], right_node[1]) + 1
        merged_depth_min = min(left_node[2], right_node[2]) + 1

        # Push the new merged node back into the heap
        heapq.heappush(heap_data,(merged_freq, merged_depth_max, merged_depth_min))
        # Update max_depth and min_depth
        max_depth = max(max_depth, merged_depth_max)
        min_depth = min(max_depth, merged_depth_min)

    # If min_depth was never updated, it means there was only one node
    if min_depth == float("inf"):
        min_depth = max_depth  # Set min_depth equal to max_depth in that case
    return max_depth, min_depth


#Question3:
def read_weights_from_file(filename):
    """Read weights from a specified file.

    Args:
        filename (str): Path to the input file containing weights.

    Returns:
        list: A list of integer weights (frequencies of symbols).
    """
    with open(filename) as f:
        next(f)  # Skip the number of symbols
        data = f.readlines()

    # Convert lines to integers and strip whitespace
    weights = [int(line.strip()) for line in data]
    return weights

def compute_max_weights(weights):
    """Compute the maximum weights using dynamic programming.

    Args:
        weights (list): A list of integer weights.

    Returns:
        list: DP list containing maximum weights up to each index.
    """
    DP = [0] * len(weights)

    # Base cases
    DP[0] = weights[0]
    if len(weights) > 1:
        DP[1] = max(weights[0], weights[1])

    for i in range(2, len(weights)):
        DP[i] = max(DP[i - 1], weights[i] + DP[i - 2])

    return DP

def backtrack_included_indices(DP):
    """Backtrack to find the included indices.

    Args:
        DP (list): DP list containing maximum weights.

    Returns:
        list: Indices of the included weights.
    """
    inclu = []
    i = len(DP) - 1
    while i >= 1:
        if DP[i] == DP[i - 1]:  # Excluded vertex
            i -= 1
        else:
            inclu.append(i + 1)  # Store 1-indexed
            i -= 2

    if i == 0:
        inclu.append(1)  # Include the first element

    return sorted(inclu)

def generate_binary_string(included_indices, target_vertices):
    """Generate a binary string representation of included indices.

    Args:
        included_indices (list): List of included indices.
        target_vertices (list): List of target vertices to check against.

    Returns:
        str: Binary string representation.
    """
    return "".join("1" if vertex in included_indices else "0" for vertex in target_vertices)

def main():
    """Main function to execute the Huffman coding implementation."""
    #Q1 and Q2 for max and min length of a codeword
    weights = parse_data_q1("test_case.txt")
    max_depth, min_depth = huffman_implem(weights)

    #question 3
    weights2 = read_weights_from_file('q3_data_w3_DP.txt')

    if weights2:  # Proceed only if weights are successfully read
        DP = compute_max_weights(weights2)
        included_indices = backtrack_included_indices(DP)
        target_vertices = [1, 2, 3, 4, 17, 117, 517, 997]
        binary_string = generate_binary_string(included_indices, target_vertices)

        print(f"Binary String: {binary_string}")


if __name__ == '__main__':
    main()