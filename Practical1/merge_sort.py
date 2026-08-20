import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original Array:", arr)

start_time = time.perf_counter()

sorted_arr = merge_sort(arr)

end_time = time.perf_counter()

print("Sorted Array:", sorted_arr)
print("Execution Time:", end_time - start_time, "seconds")