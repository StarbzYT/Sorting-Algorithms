----------------- Elementary Sorting Algorithms ----------------

What is sorting?

Sorting is the process of rearranging the items in a collection (e.g. an array) so that the items are in some kind of order.

Examples:
Sorting numbers from smallest to largest
Sorting names alphabetically
Sorting movies based on release year
Sorting movies based on revenue

Why do we need to learn this?
Sorting is an incredibly common task, so it is good to know how it works (very common in technical interviews).
There are many different ways to sort things, and different techniques have their own advantages and disadvantages (some have better/worse perfomances depending on the nature of the collection).

Objectives:

Implement bubble sort
Implement selection sort
Implement insertion sort
Understand why it is important to learn these simplier sorting algorithms

Bubble Sort:

A sorting algorithm where the largest values bubble up to the top! A key functionality when bubble sorting is swapping. When the values are compared (shifting greater with less), swap the two values and continue comparing until the array is sorted.

Time Complexity (Bubble Sort):

Since a nested loop is used, the TC is O(n^2) (worst/average case). However, if the list is almost sorted (best case), then we iterate through the list in a linear fashion, only going through it one more time AFTER it is sorted. As a result, the TC can be represented as O(2n), which is simplfied to O(n).

Selection Sort:

Similar to bubble sort, but instead of first placing large values into sorted position, it places small values in sorted position.

Time Complexity (SS):

Number of comparisons for each item is the same as bubble sort , BUT it requires less swapping (only once per cycle). A nested for loop means that as the size of the input grows, the time grows roughly in proportion to n^2 (input squared). Therefore the time complexity for Selection Sort can be summarized as O(n^2).

Insertion Sort:

Builds up the sort by gradually creating a larger left half which is always sorted. (inserts values into correct index instead of swapping once through each cycle)

Time Complexity (IS):

Quadratic time (nested loop), therefore, O(n^2) similiar to the ones above (worst case: [4, 3, 2, 1]). However, if the list is nearly sorted ([1, 2, 3, 4, -1]), Insertion Sort is by far better than the other elementary sorting algorithms as it only needs to insert the values at the correct index. For online algorithms (data that is being updated instead of already being set in stone), Insertion Sort does not care were the unsorted value(s) is/are because it only needs to insert it/them into the correct place.

Space Complexity (all):

Bubble, Selection, and Insertion sort are all O(1) or constant space for space complexity. None require copies of the given list or assigning a variable for each index.

--------------- Intermediate Sorting Algorithms --------------

Objectives:

Understand the limitations of the sorting algorithms we have learned so far (slow...)
Implement merge sort
Implement quick sort
Implement radix sort

Why learn this?

The sorting algorithms we have learned so far do not scale well
Try out bubble sort on an array of 100000 elements, it will take quite SOME time.

Faster Sorts:

There is a family of sorting algorithms that can improve time complexity from O(n^2) to O(n log n or log n^n)
There is a tradeoff between efficiency and simplicity
The more efficient algorithms are much less simple, and generally take longer to understand
