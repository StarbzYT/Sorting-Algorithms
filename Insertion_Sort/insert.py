# start by picking the second element in the array
# now compare the second element with the one before it and swap if necessary
# continue to the next element and if it is in the incorrect order, iterate through
# the sorted portion (i.e. the left side) to place the element in the correct place
# repeat until the array is sorted


def insertion(arr):
    # iterate through list
    for i in range(1, len(arr)):  # start at first index to compare to index 0 (first comparison)
        current_val = arr[i]  # place holder
        j = i - 1  # left sorted portion
        while j >= 0 and arr[j] > current_val:  # only shift if j index item is greater than current val
            arr[j+1] = arr[j]  # shift one index ahead for items that are greater than current val
            j -= 1
        arr[j+1] = current_val  # inserted item becomes new current val which means all items before it are sorted
        print(arr)
    return arr


print(insertion([2, 1, 9, 76, 4]))  # [1, 2, 4, 9, 76]
print(insertion([45, 56, 74, 2, 8, 234]))  # [2, 8, 45, 56, 74, 234]







