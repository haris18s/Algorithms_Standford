#! usr/bin/env python3

"""Median finder algorithm that claculates median each time,  in a stream of numbers. It returns
sum of  medians % 10000.
This script uses in built library heapq, to perform heap modificatiosn"""


import heapq

class MedianFinder_me1:
    """
    Median finder problem, using the heapq library which supports only min-heap operations.
    To simulate max-heap behavior, we use negative values.
    """
    def __init__(self):
        """Initializes the MedianFinder with two heaps:
        - max_heap: A max-heap (simulated using negative values) for the lower half of the numbers.
        - min_heap: A min-heap for the upper half of the numbers.
        - median_sum: A cumulative sum of all medians calculated.
        """

        self.max_heap = []  # max heap for the lower half
        self.min_heap = []  # min heap for the upper half
        self.median_sum = 0
    def add_num(self, num):
        """
        Adds a new number to the data structure and maintains the balance between the two heaps.
        Parameters:
            num (int): The number to add to the data structure.
        """
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Rebalance heaps if necessary
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


        if len(self.max_heap) >= len(self.min_heap):
            median = -self.max_heap[0]
        else:
            median = self.min_heap[0]

        # Update cumulative sum of medians
        self.median_sum += median

    def get_median_modulo(self):
        """
        Returns the sum of all medians calculated so far, modulo 10000.
        Returns:
            int: The cumulative sum of medians modulo 10000.
        """
        return self.median_sum % 10000
def main():
    # Create an instance of MedianFinder
    median_finder = MedianFinder_me1()

    with open("test_case_week_3_gaphs.txt") as f:
        numbers = f.readlines()

    for line in numbers:
        if line.rstrip() != "":
            line = line.rstrip()
            median_finder.add_num(int(line))

    # Calculate the sum of medians modulo 10000
    result = median_finder.get_median_modulo()

    print(result)


if __name__ =='__main__':
    main()