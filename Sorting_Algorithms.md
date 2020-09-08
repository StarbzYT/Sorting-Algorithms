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

Merge Sort:

Uses divide and conquer method by spliting the arrays until they are all one element each and MERGES them back together. It is a combination of two things - merging and sorting (exploits the fact that arrays of 0 or 1 element(s) are always sorted)! Works by decomposing an array into smaller arrays of 0 or 1 element(s), then building up a newly sorted array.

History:

Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output. Merge sort is a divide and conquer algorithm that was invented by John von Neumann in 1945.

Merging Arrays/Lists:

In order to implement merge sort, it is useful to first implement a function responsible for merging two sorted arrays
Given two arrays, which are sorted, this helper function should create a new array which is also sorted, and consists of all of the elements in the two input arrays
This function should run in O(n + m) time and O(n + m) space (two inputs, n and m) and should NOT modify the parameters passed to it.

Time and Space Complexity (Merge Sort):

The best, average, and worst case for the time complexity of Merge Sort is, in short, O(n log n). Take an array of 8 elements. We have to have O(log n) decompositions and O(n) comparisons per decomposition. In other words, how many steps does it take to break down an array of 8 elements (to one element each). With a base of 2, it takes 3 steps, since 2^3 is 8! Therefore, the time complexity of Merge Sort is indeed O(n log n). As for the space complexity, merge sort does require more memory to make a new sorted array compared to Bubble, Selection, and Insertion sort. As the length of input grows, merge sort requires n number of items to make a new array. As a result, the space complexity becomes O(n).

Quick Sort:

Like Merge Sort, Quick Sort exploits the fact that arrays of 0 or 1 element are always sorted. It works by selecting one element (called the "pivot") and finding the index where the pivot should end up in the sorted array. Once the pivot is positioned appropriately, Quick Sort can be applied on either side of the pivot.

Pivot Helper:

Before implementing Quick Sort, it is useful to first implement a function responsible arranging elements in an array on either side of a pivot. Given an array, this helper function should designate an element as the pivot. It should then rearrange elements in the array so that all values less than the pivot are moved to the left of it, and all values greater are moved to the right of it. The order of elements on either side of the pivot does not matter! The helper should do this IN PLACE, that is, it should not create a new array. When complete, the helper should return the index of the pivot.
