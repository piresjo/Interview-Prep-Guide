# Notes On Sorting Algorithms

## Basics

- In-place Sorting: An in-place sorting algorithm uses constant space for producing the output (modifies the given array only). Examples: Selection Sort, Bubble Sort, Insertion Sort and Heap Sort.
- Internal Sorting: Internal Sorting is when all the data is placed in the main memory or internal memory. In internal sorting, the problem cannot take input beyond allocated memory size.
- External Sorting : External Sorting is when all the data that needs to be sorted need not to be placed in memory at a time, the sorting is called external sorting. External Sorting is used for the massive amount of data. For example Merge sort can be used in external sorting as the whole array does not have to be present all the time in memory,
- Stable sorting: When two same items appear in the same order in sorted data as in the original array called stable sort. Examples: Merge Sort, Insertion Sort, Bubble Sort.
- Hybrid Sorting: A sorting algorithm is called Hybrid if it uses more than one standard sorting algorithms to sort the array. The idea is to take advantages of multiple sorting algorithms. For Example IntroSort uses Insertions sort and Quick Sort.

There are various sorting algorithms are used in data structures. The following two types of sorting algorithms can be broadly classified:

- Comparison-based: We compare the elements in a comparison-based sorting algorithm
- Non-comparison-based: We do not compare the elements in a non-comparison-based sorting algorithm.

## Bubble Sort

It is a simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order. It performs multiple passes through the array, and in each pass, the largest unsorted element moves to its correct position at the end.

After each pass, we ignore the last sorted elements and continue comparing and swapping remaining adjacent pairs. After k passes, the last k elements are sorted.

In this algorithm, in the worst case, the array being sorted is in reverse order. This leads to having to do around `n^2` comparisons and swaps. This means that the worst case time complexity is `O(n^2)`. In terms of space complexity, since the array itself is being modified, space complexity is constant.

## Insertion Sort

### What Is It?

It is a simple sorting algorithm that builds the sorted array one element at a time. It works like sorting playing cards in your hand, where each new card is inserted into its correct position among the already sorted cards.

We start with the second element, assuming the first is already sorted. If the second element is smaller, we shift the first element and insert the second in the correct position. Then we move to the third element and place it correctly among the first two. This process continues until the entire array is sorted.

### Advantages & Disadvantages

Advantages

- Simple and easy to implement.
- Stable sorting algorithm.
- Efficient for small lists and nearly sorted lists.
- Space-efficient as it is an in-place algorithm.
- Adoptive. the number of inversions is directly proportional to number of swaps. For example, no swapping happens for a sorted array and it takes `O(n)` time only.

Disadvantages

- Inefficient for large lists.
- Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases. 

### Uses

- The list is small or nearly sorted.
- Simplicity and stability are important.
- Used as a subroutine in Bucket Sort
- Can be useful when array is already almost sorted (very few inversions)
- Since Insertion sort is suitable for small sized arrays, it is used in Hybrid Sorting algorithms along with other efficient algorithms like Quick Sort and Merge Sort. When the subarray size becomes small, we switch to insertion sort in these recursive algorithms. For example IntroSort and TimSort use insertions sort.

## Selection Sort

### What Is It?

It is a comparison-based sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted part of the array and swaps it with the first unsorted element. This process continues until the array is fully sorted.

We start by finding the smallest element and swap it with the first element. Then we find the next smallest element among the remaining and swap it with the second element. This continues until all elements are placed in their correct positions.

## Merge Sort

### What Is It?

Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows the Divide and Conquer approach. It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merging them back together to obtain the sorted array. 

Here's a step-by-step explanation of how merge sort works:

- Divide: Divide the list or array recursively into two halves until it can no more be divided.
- Conquer: Each subarray is sorted individually using the merge sort algorithm.
- Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged. 

### Advantages & Disadvantages

Advantages:

- Stability : Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.
- Guaranteed worst-case performance: Merge sort has a worst-case time complexity of `O(N logN)` , which means it performs well even on large datasets.
- Simple to implement: The divide-and-conquer approach is straightforward.
- Naturally Parallel : We independently merge subarrays that makes it suitable for parallel processing.

Disadvantages:

- Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process.
- Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.
- Merge Sort is Slower than QuickSort in general as QuickSort is more cache friendly because it works in-place.

### Uses

- Sorting large datasets
- External sorting (when the dataset is too large to fit in memory)
- Used to solve problems like Inversion counting, Count Smaller on Right & Surpasser Count
- It is a preferred algorithm for sorting Linked lists.
- It can be easily parallelized as we can independently sort subarrays and then merge.
- The merge function of merge sort to efficiently solve the problems like union and intersection of two sorted arrays.

## Quick Sort

### What Is It?

QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

It works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

There are mainly three steps in the algorithm:

- Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
- Partition the Array: Re arrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.
- Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
- Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.

 There are many different choices for picking pivots.

- Always pick the first (or last) element as a pivot. The below implementation picks the last element as pivot. The problem with this approach is it ends up in the worst case when array is already sorted.
- Pick a random element as a pivot. This is a preferred approach because it does not have a pattern for which the worst case happens.
- Pick the median element is pivot. This is an ideal approach in terms of time complexity as we can find median in linear time and the partition function will always divide the input array into two halves. But it takes more time on average as median finding has high constants.

### Advantages & Disadvantages

Advantages:

- It is a divide-and-conquer algorithm that makes it easier to solve problems.
- It is efficient on large data sets.
- It has a low overhead, as it only requires a small amount of memory to function.
- It is Cache Friendly as we work on the same array to sort and do not copy data to any auxiliary array.
- Fastest general purpose algorithm for large data when stability is not required.
- It is tail recursive and hence all the tail call optimization can be done.

Disadvantages:

- It has a worst-case time complexity of `O(n^2)`, which occurs when the pivot is chosen poorly.
- It is not a good choice for small data sets.
- It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved in the sorted output in case of quick sort, because here we are swapping elements according to the pivot's position (without considering their original positions). 

### Uses

- Sorting large datasets efficiently in memory.
- Arranging records in databases for faster searching.
- Preprocessing step in algorithms requiring sorted input (e.g., binary search, two-pointer techniques).
- Finding the kth smallest/largest element using Quickselect (a variant of quicksort).
- Sorting arrays of objects based on multiple keys (custom comparators).
- Data compression algorithms (like Huffman coding preprocessing).
- Graphics and computational geometry (e.g., convex hull algorithms).

## Heap Sort

### What Is It?

FEED ME

### Advantages & Disadvantages

FEED ME

## Comparison Chart

FEED ME

## Links

[Introduction to Sorting Techniques](https://www.geeksforgeeks.org/dsa/introduction-to-sorting-algorithm/)

[Selection Sort](https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/)

[Insertion Sort Algorithm](https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/)

[Merge Sort](https://www.geeksforgeeks.org/dsa/merge-sort/)

[Heap Sort](https://www.geeksforgeeks.org/dsa/heap-sort/)