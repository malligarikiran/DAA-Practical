# Implementation of Max-Heap Sort Algorithm

def heapify(arr, n, i):
    """
    Maintains the max-heap property for the subtree
    rooted at index i.
    """
    largest = i          # Assume root is largest
    left = 2 * i + 1     # Left child
    right = 2 * i + 2    # Right child

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Sorts the array using Max-Heap Sort.
    """
    n = len(arr)

    # Step 1: Build a Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):

        # Move current maximum to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap
        heapify(arr, i, 0)


# Main program
print("MAX-HEAP SORT")
print("-------------------------")

# Take input from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("\nOriginal Array:")
print(arr)

# Perform Heap Sort
heap_sort(arr)

print("\nSorted Array:")
print(arr)