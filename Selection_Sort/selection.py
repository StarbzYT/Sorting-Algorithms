# selection sort pseudocode
# - store first element as smallest value seen so far
# - compare this item to next item in the list until you find a smaller number
# - if a smaller number is found, designate that smaller number
# to be the new "min" and continue until the end of the list
# - if the "min" is not the value (index) you initially began with, SWAP the two values!
# - repeat with next element until list is sorted


def selection(arr):
    for i in range(0, len(arr)):
        min_value = i  # set the min to be the starting point
        no_swaps = True
        print(arr)  # show arr after each cycle
        for j in range(i+1, len(arr)):  # compare starting from index infront of i to prevent comparing the same index
            if arr[j] < arr[min_value]:  # if a min value is found that is less than the starting point
                min_value = j  # set that value to be the new min
        # end of cycle
        if i != min_value:  # prevents swapping same index
            arr[i], arr[min_value] = arr[min_value], arr[i]  # swap i index with min (remember that i is not min!)
            no_swaps = False

        if no_swaps is True:  # prevents excessive comparisons. Once list is ordered and there are no swaps, break!
            break


    return arr  # return sorted array after all cycles (comparisons) are done


print(selection([34, 27, 8, 9, 23, 5]))  # [5, 8, 9, 23, 27, 34]






