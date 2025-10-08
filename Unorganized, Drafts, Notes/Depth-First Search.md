# Depth-First Search Of Graphs

## Basics

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. Extra memory, usually a stack, is needed to keep track of the nodes discovered so far along a specified branch which helps in backtracking of the graph.

### Recursive Solution

For this example, we'll be using Python. We'll be defining the graph nodes as such:

```python
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = [] # list of all connected nodes
```

You can recursively do depth-first search. Here is an example of a DFS algorithm that traverses through the entire tree.

```python
def dfs(root):
    visited = Set()
    return dfsHelper(root, visited)

def dfsHelper(root, visited):
    visited.add(root)
    for x in root.adjacent:
        if x not in visited:
            return dfsHelper(x, visited)
    return visited
```

## Iterative Solution

Once again, we'll be using python and  the `GraphNode` object

Given some data and the root of the graph, we can try to find that node in the graph like this:

```python
def dfs(root, matchData):
    visited = Set()
    stack = []

    stack.append(root)
    visited.add(root)
    while stack:
        nodeVal = stack.pop()

        if nodeVal.data == matchData:
            return nodeVal
        
        for x in nodeVal.adjacent:
            if x not in visited:
                stack.append(x)
                visited.add(x)
    return None

```

The stack is now made explicitly (in the form of a stack data structure, represented here as a list). If you've noticed, the iterative solution is quite similar to breadth-first search, with two differences:

- It uses a stack instead of a queue
- It delays checking whether a vertex has been discovered until the vertex is popped from the stack rather than making this check before adding the vertex.

## Properties

For this section, we're analyzing algorithms that traverse the whole tree.

Big N analysis is the same for either recursive or iterative implementations.

For performance, the worst case scenario is `O(V + E)`, with `V` being the number of nodes, and `E` being the number of edges.

For space, the worst case is `O(V)`, since every node needs to be accessed. This is made particularly explicit in the iterative version.

## Links

[Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search)