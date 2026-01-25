"""
General idea: we need to use DFS to get the leaves in proper order
(BFS will also take what layer the leaf is into account, which
would screw up the order). Then you can just compare the lists.
For ease, we're passing the sequences into the aux method so they
get modified, since passing in a list is passing in by reference.
"""


def leafSimilar(root1, root2) -> bool:
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False

    sequenceA = []
    sequenceB = []
    leafSimilarAux(root1, sequenceA)
    leafSimilarAux(root2, sequenceB)

    return sequenceA == sequenceB


def leafSimilarAux(root, sequence):
    if not root:
        return
    if not root.left and not root.right:
        sequence.append(root.val)
    leafSimilarAux(root.left, sequence)
    leafSimilarAux(root.right, sequence)
    return
