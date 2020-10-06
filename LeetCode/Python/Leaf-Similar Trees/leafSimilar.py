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