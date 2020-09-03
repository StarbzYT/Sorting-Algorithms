import merging_arrays  # merge func to merge two sorted arrays
# Pseudocode
# Break up the array into halves until you have arrays that are empty or have one element
# Once you have smaller sorted arrays, merge those arrays with other
# sorted arrays until you are back at the full length of the array
# once the array has been merged back together, return the merged (and sorted!) array


def merge(arr):
    if len(arr) <= 1:  # base case
        return arr
    mid = len(arr) // 2  # floored
    left = merge(arr[0:mid])  # 0 to mid (exclusive)
    right = merge(arr[mid::])  # mid to end
    return merging_arrays.merge(left, right)  # keep merging left and right sorted arrays


print(merge([1, 18, 6, 41, 3, 100]))  # [1, 3, 6, 18, 41, 100]




