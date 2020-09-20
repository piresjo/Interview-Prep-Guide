import unittest
from bubblesort import *

class Test(unittest.TestCase):
    
    def testWithNone(self):
       self.assertEqual(bubbleSort(None), None)

    def testWithEmpty(self):
       self.assertEqual(bubbleSort([]), [])

    def testWithOne(self):
       self.assertEqual(bubbleSort([1]), [1])

    def testGeneralCase(self):
        self.assertEqual(bubbleSort([9, 6, 8, 3, 1]), [1, 3, 6, 8, 9])

      

if __name__ == '__main__':
   unittest.main()
