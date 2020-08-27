--------- Elementary Sorting Algorithms ---------

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

Time Complexity:

Number of comparisons for each item is the same as bubble sort , BUT it requires less swapping (only once per cycle). A nested for loop means that as the size of the input grows, the time grows roughly in proportion to n^2 (input squared). Therefore the time complexity for Selection Sort can be summarized as O(n^2).

Insertion Sort:

Builds up the sort by gradually creating a larger left half which is always sorted. (inserts values into correct index instead of swapping once through each cycle)
