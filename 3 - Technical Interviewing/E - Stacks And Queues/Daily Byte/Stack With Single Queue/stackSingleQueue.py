class Stack:
    def __init__(self):
        self.queue = []

    def push(self, x):
        sizeVal = len(self.queue)
        self.queue.append(x)
        for i in range(0, sizeVal):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]
