# Top Algorithms and Data Structures You Really Need To Know

## Searching

Roughly speaking, there are two categories of search algorithms you’ll need to know right away: linear and binary. Depth First Search (DFS) and Breadth First Search (BFS) are also super-important, but we’ll save them for the graph traversal section below.

### Linear Search

The linear and binary algorithms are named as such to describe how long (time complexity) a search is going to take based on the size of the input that is being search.

For example, with linear search algorithms, if you have 100 items to search then the worst case scenario would require that you look at every item in the input before you came across your desired value. It is called linear because the time is takes to search is exactly correlated with the amount of items in the search (100 items/input =100 checks/complexity)

In short, linear = simple (there is nothing clever about the algorithm). For example: imagine you’re trying find your friend Lin among a line of people standing in no particular order. You already know what Lin looks like, so you simply have to look at each person, one by one, in sequence, until you recognize or fail to recognize Lin.

### Binary Search

Binary search gets its name because the word binary means “of or relating to 2 things” and the algorithm works by splitting the input into two parts until it finds the item that is being searched. One half contains the search item and the other half doesn’t. The process continues until the spot where the input is split becomes the item that is being searched. Binary search is basically just a highly disciplined approach to the process of elimination. It’s faster than linear search, but it only works with ordered sequences.

## Sorting

Ordering, otherwise know as sorting, lists of items is one of the most common programming tasks you’ll do as a developer. Here we look at two of the most useful sorting algorithms: MergeSort and QuickSort.

### MergeSort

Let’s suppose that rather than coming across the ordered line of people in the example above, you need to create an ordered line of people out of an unordered group. You don’t have much time, so you come up with a strategy to speed things up.

You first have the group of people, which are all huddled together, divide into two. Then you have each of the two groups divide into two again, and so on, until you are dealing entirely with individuals. You then begin to pair the individuals up, and have the taller of the two in each pair stand to the right of the other one. Pretty soon everyone is organized into these left-right ordered pairs.

Next, you start merging the ordered pairs into ordered groups of four; then merging the ordered groups of four into ordered groups of eight; and so on. Finally, you find that you have a complete, height-ordered line of people, just like the one you encountered above. Without knowing it, you have followed the MergeSort algorithm to accomplish your feat.

### Cheat Sheet - Sorting Algorithms

#### Comparison Based

Heap sort: When you don’t need a stable sort and you care more about worst case performance than average case performance. It’s guaranteed to be O(N log N), and uses O(1) auxiliary space, meaning that you won’t unexpectedly run out of heap or stack space on very large inputs.

Introsort: This is a quick sort that switches to a heap sort after a certain recursion depth to get around quick sort’s O(N²) worst case. It’s almost always better than a plain old quick sort, since you get the average case of a quick sort, with guaranteed O(N log N) performance. Probably the only reason to use a heap sort instead of this is in severely memory constrained systems where O(log N) stack space is practically significant.

Insertion sort: When N is guaranteed to be small, including as the base case of a quick sort or merge sort. While this is O(N²), it has a very small constant and is a stable sort.

Bubble sort, selection sort: When you’re doing something quick and dirty and for some reason you can’t just use the standard library’s sorting algorithm. The only advantage these have over insertion sort is being slightly easier to implement.

Quick sort: When you don’t need a stable sort and average case performance matters more than worst case performance. A quick sort is O(N log N) on average, O(N²) in the worst case. A good implementation uses O(log N) auxiliary storage in the form of stack space for recursion.

Merge sort: When you need a stable, O(N log N) sort, this is about your only option. The only downsides to it are that it uses O(N) auxiliary space and has a slightly larger constant than a quick sort. There are some in-place merge sorts, but AFAIK they are all either not stable or worse than O(N log N). Even the O(N log N) in place sorts have so much larger a constant than the plain old merge sort that they’re more theoretical curiosities than useful algorithms.

#### Non-Comparison Based

Counting sort: When you are sorting integers with a limited range.

Radix sort: When log(N) is significantly larger than K, where K is the number of radix digits.

Bucket sort: When you can guarantee that your input is approximately uniformly distributed.

## Trees

You’re going to see a lot of trees in your time, as they’re one of the most common data structures out there. They’re also one of the easiest data structures to picture and make sense of. Almost all of the terminology surrounding trees comes from the notion of a family tree. Depending on the position of a node (i.e. a family member) relative to other nodes in the tree, the node is called a parent, a child, a sibling, an ancestor, a descendant, etc.

## Graphs

If you want to get technical, a tree is ultimately just a special case of a graph. So it’s no surprise that graphs are everywhere in daily life and computer science. In particular, graph traversal is a big deal, and there are two algorithms you’ll want to get a handle on quick: Breadth First Search (BFS) and Depth First Search (DFS). To get a sense of what these two essential algorithms entail, imagine you’re at the top of a skyscraper shaped like a pyramid, and you need to search the whole building to find your friend Fiz. Then you realize that the pyramid is roughly equivalent to a graph where each room is a node.

### Breadth First Search

If you traverse the pyramid floor by floor, starting with the top of the pyramid, you will be roughly performing a breadth-first search for your friend Fiz

### Depth First Search

Rather than going floor by floor, if you go elevator-by-elevator, checking the nearest rooms on each stop as you traverse the pyramid in vertical slices, you will be roughly performing a depth-first search for your friend Fiz.

## Dynamic Programming

If you’re facing an enormous, heavyweight programming problem that you can’t imagine solving on your own, Dynamic programming (DP) may come to your rescue. DP will help you turn the big problem into small sub-problems. Each time DP solves one of the sub-problems, it saves the results, and eventually puts all the results it’s saved together in order to tackle the big one.

## Hashing

In recent years, there has been a sea change in how we find data. While the primary approach was once binary search, it’s now increasingly becoming the hash lookup. Although we’ll spare you the time-complexity comparison here, suffice it to say that when it comes to searching through lists with millions of items, hashing is often far faster.

## String Pattern Matching

If you’ve heard of regular expressions (aka regex), you’ve already heard of string pattern matching. The idea here is that you’re not so much searching for an item, but a pattern that may be common to lots of items. For example, suppose you are searching a book for all sentences that end in a question mark: that’s a job for string pattern matching.

## Links

[Top Algorithms and Data Structures You Really Need To Know](https://medium.com/data-science/top-algorithms-and-data-structures-you-really-need-to-know-ab9a2a91c7b5)
