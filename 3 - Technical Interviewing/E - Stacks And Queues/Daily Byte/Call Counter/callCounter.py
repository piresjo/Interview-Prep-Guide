class CallCounter:
    def __init__(self) -> None:
        self.callQueue = []

    def ping(self, t):
        self.callQueue.append(t)
        while self.callQueue[0] < (t - 3000):
            self.callQueue.pop(0)
        return len(self.callQueue)
