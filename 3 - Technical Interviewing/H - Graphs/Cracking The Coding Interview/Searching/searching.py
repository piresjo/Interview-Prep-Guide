# Perform DFS
# I'm more used to the iterative version
# Need to also implement the recursive version
def dfs(root):
    stack = []
    stack.append(root)
    discovered = set()
    while len(stack) != 0:
        nodeVal = stack.pop()
        print(nodeVal.data)
        if nodeVal not in discovered:
            discovered.add(nodeVal)
            for adjacent in nodeVal:
                stack.append(adjacent)


# Perform BFS
def bfs(root):
    queue = []
    queue.append(root)
    discovered = set()
    discovered.add(root)
    while len(queue) != 0:
        nodeVal = queue.pop(0)
        print(nodeVal.data)
        for adjacent in nodeVal.adjacent:
            if adjacent not in discovered:
                discovered.add(adjacent)


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = []

    def addEdge(self, nodeVal):
        if nodeVal in self.adjacent:
            return
        self.adjacent.append(nodeVal)
