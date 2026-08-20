import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original Array:", arr)

start_time = time.perf_counter()

insertion_sort(arr)

end_time = time.perf_counter()

print("Sorted Array:", arr)
print("Execution Time:", end_time - start_time, "seconds")