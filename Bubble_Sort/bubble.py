# BubbleSort Pseudocode
# Start looping from the end of the array with a variable called i, moving towards the beginning
# Start an inner loop with a variable called j from the beginning until i - 1
# If arr[j] is greater than arr[j+1], swap those two values!
# Return the sorted array


def bubble(arr):
    l = len(arr)  # end pointer
    for i in range(l - 1):  # forward counter from first index
        no_swaps = True  # at the beg. of cycle, set to true
        print(arr)
        for j in range(0, l-i-1):  # prevents comparing "set in stone" values and comparing out of range indices
            if arr[j] > arr[j + 1]:  # compare if index before is greater than index after
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # SWAP!
                no_swaps = False  # if values are swapped, then the list is not ordered
        # if through a whole cylce, there is no swap, then we break to prevent "useless comparisons"
        if no_swaps:
            break
    return arr  # return sorted array


print(bubble([3, 57, 97, 24, 13]))  # [3, 13, 24, 57, 97]
print(bubble([8, 1, 2, 3, 4, 5, 6, 7]))  # almost already ordered!
# ^^ only one more cycle to see if list is ordered then we break!






