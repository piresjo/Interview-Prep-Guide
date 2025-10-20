# Understanding Binary Heaps

A Binary Heap is a complete binary tree that stores data efficiently, allowing quick access to the maximum or minimum element, depending on the type of heap. It can either be a Min Heap or a Max Heap. In a Min Heap, the key at the root must be the smallest among all the keys in the heap, and this property must hold true recursively for all nodes. Similarly, a Max Heap follows the same principle, but with the largest key at the root.

A Binary Heap is a Complete Binary Tree. A binary heap is typically represented as an array.

Here's an example. Let's say we have the heap (represented as a tree)

```
          1
        /   \
    3           6
  /   \       /
5       9   8
```

It can be represented as an array like this:

```python
[1, 3, 6, 5, 9, 8]
```

Applications Include:

Heap Sort: Heap Sort uses Binary Heap to sort an array in O(nLogn) time.
Priority Queue: Priority queues can be efficiently implemented using Binary Heap because it supports insert(), delete() and extractmax(), decreaseKey() operations in O(log N) time. Binomial Heap and Fibonacci Heap are variations of Binary Heap. These variations perform union also efficiently.
Graph Algorithms: The priority queues are especially used in Graph Algorithms like Dijkstra's Shortest Path and Prim's Minimum Spanning Tree.

## Links

[Binary Heap](https://www.geeksforgeeks.org/dsa/binary-heap/)