def findMode(root):
    if root is None:
        return []

    modes = []
    traverse(root, modes, None, 1, 0)
    return modes


def traverse(self, root, modes, prev, count, maxVal):
    if root is None:
        return

    self.traverse(root.left, modes, prev, count, maxVal)

    if prev is not None:
        if prev == root.val:
            count += 1
        else:
            count = 1

    if count > maxVal:
        modes.clear()
        modes.append(root.val)
        maxVal = count
    elif count == maxVal:
        modes.append(root.val)

    prev = root.val
    traverse(root.right, modes, prev, count, maxVal)
