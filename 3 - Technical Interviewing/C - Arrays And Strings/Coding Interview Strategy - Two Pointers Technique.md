# Two Pointers Technique

The Two-Pointers Technique is a simple yet powerful strategy where you use two indices (pointers) that traverse a data structure—such as an array, list, or string—either toward each other or in the same direction to solve problems more efficiently

Two pointers is really an easy and effective technique that is typically used for Two Sum in Sorted Arrays, Closest Two Sum, Three Sum, Four Sum, Trapping Rain Water and many other popular interview questions.

## Motivation

To show the usefulness of the two pointer technique, let's look at a naive solution to a problem and see how we can improve it.

Let's say you have a sorted array `arr`. Can you find a pair of elements that equal `sum`?

A naive solution would involve checking all pair combinations (the order of the pairs don't count, of course). If you were to code this, the solution would involve a nested loop:

```python
def findSumPair(arr, sum):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

Nested loops over an array always yield a `O(n^2)` time complexity.

## What The Two Pointers Technique Is

There is a way to shrink the time complexity to `O(n)`. We need two pointers again, but we're not doing a nested loop.

Instead, one pointer will be at the beginning of the array and the other pointer will be at the end. We can dop that because when dealing with all possible combinations for the sum, we can forgo the order of the numbers. Then we can adjust one or more of the pointers to get to the sum.

```python
def findSumPair(arr, sumTarget):
    left = 0
    right = len(arr) - 1

    while left < right:
        tempSum = (arr[left] + arr[right])
        if tempSum == sumTarget:
            return True
        elif tempSum < sumTarget:
            left += 1
        else:
            right -= 1
```

## When To Use It

- Sorted Input : If the array or list is already sorted (or can be sorted), two pointers can efficiently find pairs or ranges. Example: Find two numbers in a sorted array that add up to a target.
- Pairs or Subarrays : When the problem asks about two elements, subarrays, or ranges instead of working with single elements. Example: Longest substring without repeating characters, maximum consecutive ones, checking if a string is palindrome.
- Sliding Window Problems : When you need to maintain a window of elements that grows/shrinks based on conditions. Example: Find smallest subarray with sum ≥ K, move all zeros to end while maintaining order.
- Linked Lists (Slow–Fast pointers) : Detecting cycles, finding the middle node, or checking palindrome property. Example: Floyd’s Cycle Detection Algorithm (Tortoise and Hare).

## Links

[Two Pointers Technique](https://www.geeksforgeeks.org/dsa/two-pointers-technique/)