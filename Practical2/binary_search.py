import time

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


# Main Program
print("===== BINARY SEARCH =====")

n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

# Sort the array
arr.sort()

print("\nSorted Array:", arr)

target = int(input("Enter element to search: "))

# Start time
start_time = time.perf_counter()

position, comparisons = binary_search(arr, target)

# End time
end_time = time.perf_counter()

execution_time = end_time - start_time

# Display result
if position != -1:
    print("\nElement found!")
    print("Position in sorted array:", position + 1)
else:
    print("\nElement not found!")

print("Number of comparisons:", comparisons)
print("Execution time:", execution_time, "seconds")

print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(log n)")
print("Worst Case   : O(log n)")