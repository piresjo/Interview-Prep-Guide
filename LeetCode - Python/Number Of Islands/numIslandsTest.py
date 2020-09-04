import unittest
from numIslands import *

class Test(unittest.TestCase):
    def testEdgeCases(self):
        self.assertEqual(numIslands(None), 0)
        #self.assertEqual(numIslands([1]), 0)
        self.assertEqual(numIslands([]), 0)

    def testIslands(self):
        island1 = [["1", "1", "0"], ["1", "0", "1"], ["0", "1", "1"]]
        island2 = [["1", "0", "1"], ["1", "0", "0"], ["0", "1", "1"]]

        self.assertEqual(numIslands(island1), 2)
        self.assertEqual(numIslands(island2), 3)


   

if __name__ == '__main__':
   unittest.main()