# Tree Traversals

A subgroup of graph traversals are tree traversals. These apply the principles of both Depth-First Search and Breadth-First Search to visit each node in a tree.

For our code samples and examples, we'll be focusing on binary trees. For other types of trees, the algorithm can be slightly modified to deal with more than two connections.

We're defining the `TreeNode` as such:

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

We can provide a `Tree` of `TreeNode`s by providing the root node of the tree.

The constraints of the tree (namely the acyclic nature and the fact that aside from the head node each node has only one parent) lend it to recursive algorithms (with the exception of level-order traversals).

## Pre-Order Traversal

The pre-order traversal goes through the tree in this order: Root -> Left -> Right

```python
def preOrder(head):
    if head is None:
        return

    print str(head.data) + ' '
    preOrder(head.left)
    preOrder(head.right)
```

Suppose we have the tree

```
            4
          /   \
        2       6
      /   \    /  \
    1       3 5     7
```

The traversal yields us:

```python
[4, 2, 1, 3, 6,  5, 7]
```

## Post-Order Traversal

The post-order traversal goes through the tree in this order: Left -> Right -> Root

```python
def postOrder(head):
    if head is None:
        return

    postOrder(head.left)
    postOrder(head.right)
    print str(head.data) + ' '
```

Suppose we have the tree:

```
            4
          /   \
        2       6
      /   \    /  \
    1       3 5     7
```

The traversal yields us:

```python
[1, 3, 2, 5, 7, 6, 4]
```

## In-Order Traversal

The in-order traversal goes through the tree in this order: Left -> Root -> Right

```python
def inOrder(head):
    if head is None:
        return

    inOrder(head.left)
    print str(head.data) + ' '
    inOrder(head.right)
```

Suppose we have the tree:

```
            4
          /   \
        2       6
      /   \    /  \
    1       3 5     7
```

The traversal yields us:

```python
[1, 2, 3, 4, 5, 6, 7]
```

## Level-Order Traversal

```python
def levelOrder(head):
    queue = []
    temp = head

    while temp is not None:
        print str(temp.data) + ' '
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
        
        temp = queue.pop(0)
```

Suppose we have a tree:

```
            4
          /   \
        2       6
      /   \    /  \
    1       3 5     7
```

The traversal yields us:

```python
[4, 2, 6, 1, 3, 5, 7]
```

## Links

[Tree traversal](https://en.wikipedia.org/wiki/Tree_traversal)

[Tree Traversal Techniques](https://www.geeksforgeeks.org/dsa/tree-traversals-inorder-preorder-and-postorder/)