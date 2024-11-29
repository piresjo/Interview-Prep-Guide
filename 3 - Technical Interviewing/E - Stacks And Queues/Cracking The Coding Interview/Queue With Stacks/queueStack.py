class QueueStack:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def enqueue(self, x):
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        
        self.stackA.append(x)

        while self.stackB:
            self.stackA.append(self.stackB.pop())

    def dequeue(self):
        if len(self.stackA) == 0:
            return None
        return self.stackA.pop()