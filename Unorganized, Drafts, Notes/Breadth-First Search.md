# Breadth-First Search Of Graphs

## Basics

Breadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored. 

## Iterative Solution

For this example, we'll be using Python. We'll be defining the graph nodes as such:

```python
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = [] # list of all connected nodes
```

Once again, we'll be using python and  the `GraphNode` object

Given some data and the root of the graph, we can try to find that node in the graph like this:

```python
def bfs(root, matcher):
    visited = Set()
    queue = []

    queue.append(root)
    visited.add(root)

    while queue:
        nodeVal = queue.pop(0)
        if nodeVal.data == matcher:
            return nodeVal

        for x in nodeVal.adjacent:
            if x not in visited:
                queue.append(x)
                visited.add(x)
    return None

```

If you've noticed, the iterative solution is quite similar to depth-first search, with two differences:

- It uses a queue instead of a stack
- It checks the vertex before adding it, rather than in reverse.

## Properties

For this section, we're analyzing algorithms that traverse the whole tree.

For performance, the worst case scenario is `O(V + E)`, with `V` being the number of nodes, and `E` being the number of edges.

For space, the worst case is `O(V)`, since every node needs to be accessed.

## Links
[Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)