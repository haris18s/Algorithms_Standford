#! usr/bin/env python3
import sys


def parse_knapsack_file(filename):
    """Parses the input file. First line has knapsack size and number of items.
    Each subsequent line has value and weight for each object.

    Args:
        filename (str): Path to the input text file.

    Returns:
        tuple: Knapsack size, number of items, list of values, list of weights.
    """
    with open(filename) as f:
        #read first line
        first_line = f.readline().rstrip().split()
        knapsack_size, items = int(first_line[0]), int(first_line[1])

        data = f.readlines()
    values = []
    weights = []
    for line in data:
        line = line.rstrip().split()
        values.append(int(line[0]))
        weights.append(int(line[1]))

    return knapsack_size,items, values, weights



def knapsack_q1(knapsack_capacity, items, values, weights):
    """Function to calcluate the max value for knapsack problem when no of items is relative  small.


    Input:
        knapsack_capacity(int): maximum capacity of knapsack,
        no_items(int): The number of items available
        (list) of values: A list containg the values of items
        (list) of weights: a list containg the weights of the items
    Output:
        (int) the max value
    """

    #create the 2D array to fill the values
    arr = [[0] * (knapsack_capacity+ 1) for _ in range(items+1)]

    for i in range(items+1):
        for w in range(knapsack_capacity + 1):
            if i ==  0 or w == 0:
                arr[i][w] = 0
            elif weights[i-1] <= w:
                arr[i][w] =  max(values[i-1] + arr[i-1][w-weights[i-1]], arr[i-1][w])
            else:
                arr[i][w] = arr[i-1][w]

        # return the max value that can be put in the knapsack of capacity 'knapsack capacity'
    return arr[items][knapsack_capacity]


def knapsack_recursive_memoization(knapsack_capacity, no_items, values, weights, memo=None):
    """Calculate the maximum value for the knapsack problem using recursive memoization.
        USed for quesiton 2.
    Args:
        knapsack_capacity (int): Maximum capacity of knapsack.
        no_items (int): Number of available items.
        values (list): List of values of items.
        weights (list): List of weights of items.
        memo (dict): Dictionary for memoization.

    Returns:
        int: Maximum value that can be put in the knapsack.
    """
    if memo is None:
        memo = {}  # Initialize the memoization dictionary on the first call

    # Base cases
    if no_items == 0 or knapsack_capacity == 0:
        return 0

    # Check if the result is already computed (memoization check)
    if (no_items, knapsack_capacity) in memo:
        return memo[(no_items, knapsack_capacity)]


    # If the current item's weight is more than the current capacity
    if weights[no_items - 1] > knapsack_capacity:
        result = knapsack_recursive_memoization(knapsack_capacity, no_items - 1, values, weights, memo)  # Exclude the current item
    else:
        # Include the current item or exclude it
        result = max(
            knapsack_recursive_memoization(knapsack_capacity, no_items - 1, values, weights, memo),  # Exclude the current item
            values[no_items - 1] + knapsack_recursive_memoization(knapsack_capacity - weights[no_items - 1], no_items - 1, values, weights, memo)  # Include the current item
        )

    # Store the result in the memoization cache
    memo[(no_items, knapsack_capacity)] = result

    return result
def main():

    knapsack_capacity, no_items, values, weights  = parse_knapsack_file("knapsack1_input.txt")
    max_value_q1 = knapsack_q1(knapsack_capacity, no_items,values, weights)
    print(max_value_q1)



    #Question 2
    sys.setrecursionlimit(3000)
    knapsack_capacity, no_items, values, weights  = parse_knapsack_file("knapsack_big_wk2_project_q2.txt")

    # Calculate maximum value using recursive memoization
    max_value_q2 = knapsack_recursive_memoization(knapsack_capacity,no_items,values,weights)
    print(max_value_q2)


if __name__ == '__main__':
    main()