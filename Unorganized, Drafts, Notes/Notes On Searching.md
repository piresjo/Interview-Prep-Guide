# Notes On Searching

## Linear Searching

Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

In Linear Search, we iterate over all the elements of the array and check if it the current element is equal to the target element. If we find any element to be equal to the target element, then return the index of the current element. Otherwise, if no element is equal to the target element, then return -1 as the element is not found. Linear search is also known as sequential search.

In terms of space complexity, it is constant. In terms of time complexity, since

### Applications

- Unsorted Lists: When we have an unsorted array or list, linear search is most commonly used to find any element in the collection.
- Small Data Sets: Linear Search is preferred over binary search when we have small data sets with
- Searching Linked Lists: In linked list implementations, linear search is commonly used to find elements within the list. Each node is checked sequentially until the desired element is found.
- Simple Implementation: Linear Search is much easier to understand and implement as compared to Binary Search or Ternary Search.

### Advantages

- Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays of any data type.
- Does not require any additional memory.
- It is a well-suited algorithm for small datasets.

### Disadvantages

- Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
- Not suitable for large arrays.

## Binary Searching

Binary Search is a searching algorithm that operates on a sorted or monotonic search space, repeatedly dividing it into halves to find a target value or optimal answer in logarithmic time O(log N).

To apply Binary Search algorithm:

- The data structure must be sorted.
- Access to any element of the data structure should take constant time.

## Other Forms Of Searching

These don't need to be studied, but it's good to know

### Ternary Search

Ternary Search is a variant of binary search that splits the search interval into three parts instead of two.

### Jump Search

Jump Search is another searching algorithm that can be used on sorted collections (arrays or lists). The idea is to reduce the number of comparisons by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

### Interpolation Search

Interpolation Search is an efficient searching algorithm for sorted collections of data, such as arrays or lists. It is an improvement over Binary Search, particularly when the data is uniformly distributed.

### Fibonacci Search

Fibonacci Search is an efficient searching algorithm used for finding a target value in a sorted collection, such as an array or list. It is similar in principle to Binary Search but uses Fibonacci numbers to determine the positions to be compared.

### Exponential Search

Exponential Search is a searching algorithm designed to find a target value in a sorted collection, such as an array or list. It combines elements of Binary Search and Linear Search to efficiently locate the target, especially when its position is near the beginning of the collection.

## Comparing Different Types Of Searching

|       Algorithm      | Best Case | Average Case | Worst Case | Space |     Requirement     |
|:--------------------:|:---------:|:------------:|:----------:|:-----:|:-------------------:|
| Linear Search        | O(1)      | O(N)         | O(N)       | O(1)  | Works on any data   |
| Binary Search        | O(1)      | O(log N)     | O(log N)   | O(1)  | Sorted array needed |
| Ternary Search       | O(1)      | O(log₃ N)    | O(log₃ N)  | O(1)  | Unimodal data       |
| Jump Search          | O(1)      | O(√N)        | O(√N)      | O(1)  | Sorted data         |
| Interpolation Search | O(1)      | O(log log N) | O(N)       | O(1)  | Uniform data        |
| Fibonacci Search     | O(1)      | O(log N)     | O(log N)   | O(1)  | Sorted data         |
| Exponential Search   | O(1)      | O(log N)     | O(log N)   | O(1)  | Sorted data         |

## Links

[Introduction to Searching](https://www.geeksforgeeks.org/dsa/introduction-to-searching-algorithms-2/)

[Linear Search Algorithm](https://www.geeksforgeeks.org/dsa/linear-search/)

[Binary Search](https://www.geeksforgeeks.org/dsa/binary-search/)