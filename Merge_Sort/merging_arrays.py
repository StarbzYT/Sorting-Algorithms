# Merging Arrays Pseudocode
# create an empty array, take a look at the smallest values in each input array
# while there are still values we have not looked at...
    # if the value in the first array is smaller than the value in the second array,
    # push the value in the first array into our results and move on to the next value in the first array
    # if the value in the first array is larger than the value in the second array,
    # push the value in the second array into our results 
    # and move on to the next value in the second array
    # once we exhaust one array, push in all remaining values from the other array


def merge(arr1, arr2):  # takes in two sorted arrays
    results = []  # sorted array (after everything is sorted)
    i = 0  # for arr1
    j = 0 # for arr2

    while i < len(arr1) and j < len(arr2):  # while elements are still in both lists/arrays
        if arr1[i] < arr2[j]:
            results.append(arr1[i])  # always append smaller value
            i += 1  # move on to next i value
        else:
            results.append(arr2[j])  # if arr2[j] is less than arr1[i]
            j += 1  # move on to next j value
    
    while i < len(arr1):  # if arr2 has reached the end, but arr1 still has values
        results.append(arr1[i])  # append everything to results
        i += 1
        
    while j < len(arr2):  # otherwise, if arr1 has reached the end, append all arr2 values to results
        results.append(arr2[j])
        j += 1
    
    return results  # final (one) sorted arr/list

# to be used for merge sort algo
if __name__ == '__main__':
    print(merge([1, 5, 17, 21], [100, 350]))  # each list MUST be sorted for this to work/combine into one list


