import time

def linear_search(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        if arr[i] == target:
            return i, comparisons

    return -1, comparisons


# Main Program
print("===== LINEAR SEARCH =====")

n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

target = int(input("Enter element to search: "))

# Start time
start_time = time.perf_counter()

position, comparisons = linear_search(arr, target)

# End time
end_time = time.perf_counter()

execution_time = end_time - start_time

# Display result
if position != -1:
    print("\nElement found!")
    print("Position:", position + 1)
else:
    print("\nElement not found!")

print("Number of comparisons:", comparisons)
print("Execution time:", execution_time, "seconds")

print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")