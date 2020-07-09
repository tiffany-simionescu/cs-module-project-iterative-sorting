def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)
    while end >= start:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        else:
            if target < arr[middle]:
                end = middle - 1
            if target > arr[middle]:
                start = middle + 1
    return -1  # not found
