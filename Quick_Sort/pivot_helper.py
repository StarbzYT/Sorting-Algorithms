# Pivot Helper Pseudocode
# It will help to accept three arguments: an array, a start index, and an end index
# (these can default to 0 and the array length minus 1, respectively)
# Grab the pivot from the start of the array (can be any index not just 0)
# Store the current pivot index in a variable (this will keep track 
# of where the pivot should end up)
# Loop through the array from the start until the end
    # If the pivot is greater than the current, increment the pivot index variable and then 
    # swap the current element with the element at the pivot index
# Swap the starting element (i.e. the pivot) with the pivot index


def pivot(arr, start=0):
    pivot = arr[start]  # value we want to swap
    swap_index = start
    for i in range(start+1, len(arr)):  # don't need to compare index 0 to itself
        if arr[pivot] > arr[i]:
            swap_index += 1  # keep count of where we need to swap pivot
    arr[swap_index], arr[i] = arr[i], arr[swap_index]  # SWAP!
    return swap_index


print(pivot([4, 8, 2, 1, 5, 7, 6, 3]))  # 3
# index 3 is where the first index is set in place
# as a result, all nums to the left of it are less and right are greater, vice versa.
