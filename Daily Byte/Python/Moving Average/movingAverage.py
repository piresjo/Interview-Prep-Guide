class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.averageList = []

    def next(self, val):
        if len(self.averageList) == self.size:
            self.averageList.pop(0)
        self.averageList.append(val)
        return sum(self.averageList) / len(self.averageList)