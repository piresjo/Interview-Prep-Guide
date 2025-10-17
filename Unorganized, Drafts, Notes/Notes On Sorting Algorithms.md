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

### Advantages & Disadvantages

## Selection Sort

### What Is It?

### Advantages & Disadvantages

## Merge Sort

### What Is It?

### Advantages & Disadvantages

## Quick Sort

### What Is It?

### Advantages & Disadvantages

## Heap Sort

### What Is It?

### Advantages & Disadvantages



## Comparison Chart

FEED ME

## Links

[Introduction to Sorting Techniques](https://www.geeksforgeeks.org/dsa/introduction-to-sorting-algorithm/)

[Selection Sort](https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/)

[Insertion Sort Algorithm](https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/)

[Merge Sort](https://www.geeksforgeeks.org/dsa/merge-sort/)

[Heap Sort](https://www.geeksforgeeks.org/dsa/heap-sort/)