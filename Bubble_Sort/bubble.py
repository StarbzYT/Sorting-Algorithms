# BubbleSort Pseudocode
# Start looping from the end of the array with a variable called i, moving towards the beginning
# Start an inner loop with a variable called j from the beginning until i - 1
# If arr[j] is greater than arr[j+1], swap those two values!
# Return the sorted array


def bubble(arr):
    l = len(arr)  # end pointer
    for i in range(l - 1):
        print(arr)
        for j in range(0, l-i-1):  # prevents comparing "set in stone" values and comparing out of range indices
            if arr[j] > arr[j + 1]:  # compare if index before is greater than index after
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # SWAP!
    return arr  # return sorted array


print(bubble([3, 57, 97, 24, 13]))  # [3, 13, 24, 57, 97]







