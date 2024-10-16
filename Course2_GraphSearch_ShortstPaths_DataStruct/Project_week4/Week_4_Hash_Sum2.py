#! usr/bin/env python3
"""
Author: Haris Spyridis
Description:
This script is for the project for the course 2 (Graph Search, Week 4) for Algorithmm Specialization  offered by
Stanford in Coursera."""


def parse_file(file_name):
    """
    Parses the input file to extract numbers.

    Input:
        file_name (str): The name of the file to read.

    Returns:
        List[int]: A list of integers parsed from the file.
    """

    with open(file_name, "r") as f:
        data = f.readlines()
    numbers = [int(line.rstrip()) for line in data if line.strip() !=""]

    return numbers


def two_sum_pointers(array, target_range):
    """
    Finds distinct sums within a specified range using the two pointers technique.

    Input:
        array (List[int]): An array of input numbers.
        target_range (List[int]): A list containing the start and end of the target range.

    Returns:
        int: The count of distinct sums that fall within the specified interval.
    """
    #sort the input array to enable pointers technique
    array.sort()

    start,end = target_range

    n = len(array)
    #two pointers at start and end of the array
    i,j = 0, n-1
    #set to store the distinct sums i.e distinct complement
    valid_sum = set()
    # Loop until the two pointers cross each other
    while i < j:
        sum = array[i] + array[j]

        #if the two nums sum out of the range of interval increment or decrement pointers
        if sum <= start:
            i +=1
        elif sum >= end:
            j -=1
        #if two nums add within interval
        else:
            #k for iterating backwards and keep j in place for all potential pairs i,j
            k = j
            # Loop backwards from the right pointer
            while k > i:
                current_sum = array[i] + array[k]
                # Break if the current sum is less than or equal to the start, as further values will only decrease
                if current_sum <= start:
                    break

                # If the current sum is within the target range
                if start <= current_sum <= end :
                    #store the valid sums as well
                    valid_sum.add(current_sum)

                    #decrement k
                    k -=1

            # Increment i to explore new pairs
            i +=1

    return len(valid_sum)

def two_sum_2nd_method(array, target_range):
    """
    Finds distinct sums within a specified range using a hash table.

    Note:
        This method is less efficient (O(n^2)) and not suitable for large inputs.

    Input:
        array (List[int]): An array of input numbers.
        target_range (List[int]): A list containing the start and end of the target range.

    Returns:
        int: The count of distinct sums that fall within the specified interval.
    """

    start, end = target_range
    hash_table = dict()
    count = 0
    # Populate the hash table with the numbers in the array
    for num in array:
        hash_table[num] = True

    # Iterate over each possible target sum in the range
    for target in range(start, end +1):
        for num in array:
            complement =  target - num
            # If the complement exists and is not the same as the current number
            if complement in hash_table and complement != num:
                count +=1
                # Break to avoid counting duplicates for the same target
                break
    return count







def main():
    data_nums = parse_file("-programming_prob-2sum_data.txt")
    target_range = [-10000,10000]
    result = two_sum_pointers(data_nums, target_range)
    print(f"The number of valid sums are {result}")




if __name__ == "__main__":
    main()
