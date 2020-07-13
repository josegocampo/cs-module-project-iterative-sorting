def linear_search(arr, target):
    # Your code here
    for num in range(0, len(arr)):
        if arr[num] == target:
            return num

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    for num in range(0, len(arr)):
        if arr[num] == target:
            return num
        median = len(arr) / 2
        arr_median_value = int(median)
        if target < arr[arr_median_value]:
            new_arr = arr[:arr_median_value]
            binary_search(new_arr, target)
        if target > arr[arr_median_value]:
            new_arr = arr[arr_median_value:]
            binary_search(new_arr, target)



    return -1  # not found
