import unittest
from queueStack import *

class Test(unittest.TestCase):

    def testGeneral(self):
        queueVal = QueueStack()

        self.assertIsNone(queueVal.dequeue())

        queueVal.enqueue(1)
        queueVal.enqueue(2)
        queueVal.enqueue(3)
        queueVal.enqueue(4)

        self.assertEqual(queueVal.dequeue(), 1)
        self.assertEqual(queueVal.dequeue(), 2)
        self.assertEqual(queueVal.dequeue(), 3)
        self.assertEqual(queueVal.dequeue(), 4)

    
if __name__ == '__main__':
   unittest.main()