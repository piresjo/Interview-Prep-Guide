class MinStack:
    def __init__(self):
        self.minVal = float("inf")
        self.stack = []
        self.minStack = []

    def push(self, x):
        if x < self.minVal:
            self.minStack.append(x)
            self.minVal = x
        self.stack.append(x)
    
    def pop(self):
        value = self.stack.pop()
        if value == self.minVal:
            self.minStack.pop()
            self.minVal = self.minStack[len(self.minStack)-1]
        return value
    
    def min(self):
        return self.minVal

