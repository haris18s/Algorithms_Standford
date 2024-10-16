#! usr/bin/env python3

"""Median finder algorithm that claculates median each time,  in a stream of numbers. It returns
sum of  medians % 10000.
This script utilizes its own heap class (instead of heapq library) to perform modifications."""



class Heap:
    def __init__(self, is_min_heap=True):
        """
            Initializes a heap as either a min-heap or max-heap.
            is_min_heap: If True, the heap acts as a min-heap. If False, it acts as a max-heap.
        """
        self.heap = []
        self.is_min_heap = is_min_heap

    def insert(self, value):
        """
            Inserts a value into the heap and maintains the heap property by bubbling it up.
            value: The value to insert into the heap.
        """
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def remove_root(self):
        """
        Removes and returns the root element of the heap (min or max depending on the type).
        Returns the root element, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        last_value = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self.bubble_down(0)
        return root

    def root(self):
        """
        Returns the root of the heap (min or max depending on the type), without removing it.
        Returns None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def bubble_up(self, index):
        """
        Moves a newly inserted element upwards to restore the heap property.
        index: The index of the element to bubble up.
        """
        while index > 0:
            parent_index = (index - 1) // 2
            if (self.heap[index] < self.heap[parent_index]) == self.is_min_heap:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    def bubble_down(self, index):
        """
        Moves an element downwards to restore the heap property after removal of the root.
        index: The index of the element to bubble down.
        """
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and (self.heap[left] < self.heap[smallest]) == self.is_min_heap:
                smallest = left
            if right < n and (self.heap[right] < self.heap[smallest]) == self.is_min_heap:
                smallest = right

            if smallest == index:
                break

            self.swap(index, smallest)
            index = smallest

    def swap(self, i, j):
        """
        Swaps two elements in the heap.
        i, j: Indices of the elements to swap.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        """
        Returns a string representation of the heap.
        """
        return str(self.heap)


class MedianFinder:
    """
    Initializes a MedianFinder that uses two heaps:
    - max_heap: A max-heap to store the smaller half of the numbers.
    - min_heap: A min-heap to store the larger half of the numbers.
    Also initializes the cumulative sum of medians (median_sum).
    """
    def __init__(self):
        # Max-heap for the lower half
        self.max_heap = Heap(is_min_heap=False)
        # Min-heap for the upper half
        self.min_heap = Heap(is_min_heap=True)
        self.median_sum = 0

    def add_num(self, num):
        """
        Adds a new number to the data structure and maintains the balance between the heaps.
        num: The number to add.
        """
        if len(self.max_heap.heap) == 0 or num <= self.max_heap.root():
            self.max_heap.insert(num)
        else:
            self.min_heap.insert(num)

        # Re-balance heaps if necessary
        if len(self.max_heap.heap) > len(self.min_heap.heap) + 1:
            self.min_heap.insert(self.max_heap.remove_root())
        elif len(self.min_heap.heap) > len(self.max_heap.heap):
            self.max_heap.insert(self.min_heap.remove_root())

        # Calculate the current median
        if len(self.max_heap.heap) >= len(self.min_heap.heap):
            median = self.max_heap.root()
        else:
            median = self.min_heap.root()

        # Update cumulative sum of medians
        #print(f"Current Median: {median}")
        self.median_sum += median

    def get_median_modulo(self):
        return self.median_sum % 10000


def main():
    # Create an instance of MedianFinder
    median_finder = MedianFinder()

    # Test input values
    test_values = [1, 666, 10, 667, 100, 2, 3]

    with open("Median_maint_data_wk3_Graphs.txt") as f:
        numbers = f.readlines()

    for line in numbers:
        if line.rstrip() != "":
            line = line.rstrip()
            median_finder.add_num(int(line))
            #print(f"Max-Heap: {median_finder.max_heap}, Min-Heap: {median_finder.min_heap}")



    # Calculate the sum of medians modulo 10000
    result = median_finder.get_median_modulo()
    print(result)

if __name__ == '__main__':
    main()