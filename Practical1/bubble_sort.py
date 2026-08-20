import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


# Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original Array:", arr)

start_time = time.perf_counter()

bubble_sort(arr)

end_time = time.perf_counter()

print("Sorted Array:", arr)
print("Execution Time:", end_time - start_time, "seconds")