import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


# Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original Array:", arr)

start_time = time.perf_counter()

sorted_arr = quick_sort(arr)

end_time = time.perf_counter()

print("Sorted Array:", sorted_arr)
print("Execution Time:", end_time - start_time, "seconds")