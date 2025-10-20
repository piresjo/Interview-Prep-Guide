# Basic Notes On Arrays

## What Are Arrays

An array is a collection of items of the same variable type that are stored at contiguous memory locations. It is one of the most popular and simple data structures used in programming.

### Basic terminologies of Array

- Array Element: Elements are items stored in an array.
- Array Index: Elements are accessed by their indexes. Indexes in most of the programming languages start from 0.

### Memory representation of Array

In an array, all the elements or their references are stored in contiguous memory locations. This allows for efficient access and manipulation of elements.

In terms of what gets filled in those contiguous memory spaces, some languages do things differently. Sometimes languages exclusively have pointers to other objects (like Python).

## Analysis Of Array Actions

FEED ME

## Applications of Arrays

Arrays mainly have advantages like random access and cache friendliness over other data structures that make them useful.

- Storing and accessing data: Arrays store elements in a specific order and allow constant-time O(1) access to any element.
- Searching: If data in array is sorted, we can search an item in O(log n) time. We can also find floor(), ceiling(), kth smallest, kth largest, etc efficiently.
- Matrices: Two-dimensional arrays are used for matrices in computations like graph algorithms and image processing.
- Implementing other data structures: Arrays are used as the underlying data structure for implementing stacks and queues.
- Dynamic programming: Dynamic programming algorithms often use arrays to store intermediate results of sub-problems in order to solve a larger problem.
- Data Buffers: Arrays serve as data buffers and queues, temporarily storing incoming data like network packets, file streams, and database results before processing.

## Advantages of Array Data Structure

- Efficient and Fast Access: Arrays allow direct and efficient access to any element in the collection with constant access time, as the data is stored in contiguous memory locations.
- Memory Efficiency: Arrays store elements in contiguous memory, allowing efficient allocation in a single block and does not require extra storage for linking different blocks.
- Versatility: Arrays can be used to store a wide range of data types, including integers, floating-point numbers, characters, and even complex data structures such as objects and pointers.
- Compatibility with hardware: The array data structure is compatible with most hardware architectures, making it a versatile tool for programming in a wide range of environments.

## Disadvantages of Array Data Structure

- Fixed Size: Arrays have a fixed size set at creation. Expanding an array requires creating a new one and copying elements, which is time-consuming and memory-intensive. Even dynamic sized arrays internally use fixed sized memory allocation and de-allocation.
- Memory Allocation Issues: Allocating large arrays can cause memory exhaustion, leading to crashes, especially on systems with limited resources.
- Insertion and Deletion Challenges: Adding or removing elements requires shifting subsequent elements, making these operations inefficient.

## Links

[Applications, Advantages and Disadvantages of Array](https://www.geeksforgeeks.org/dsa/applications-advantages-and-disadvantages-of-array-data-structure/)

[Array Introduction](https://www.geeksforgeeks.org/dsa/introduction-to-arrays-data-structure-and-algorithm-tutorials/)