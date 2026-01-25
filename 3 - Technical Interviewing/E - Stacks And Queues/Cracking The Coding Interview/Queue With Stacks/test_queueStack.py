import pytest
from queueStack import *


class Test:

    def testGeneral(self):
        queueVal = QueueStack()

        assert not queueVal.dequeue()

        queueVal.enqueue(1)
        queueVal.enqueue(2)
        queueVal.enqueue(3)
        queueVal.enqueue(4)

        assert queueVal.dequeue() == 1
        assert queueVal.dequeue() == 2
        assert queueVal.dequeue() == 3
        assert queueVal.dequeue() == 4
