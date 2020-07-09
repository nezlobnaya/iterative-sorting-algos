def linear_search(arr, target):
    # Your code here
    for index, item in enumerate(arr):
        if item == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)// 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid -1
        else:
            low = low + 1

    return -1  # not found
