import unittest
from wordSearch import *

class Test(unittest.TestCase):
    def testEdgeCases(self):
        threeByThree = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        self.assertFalse(exist(None, None))
        self.assertFalse(exist(None, "HELLO"))
        self.assertFalse(exist(threeByThree, None))
        self.assertFalse(exist(['A'], "HELLO"))

    def testSingle(self):
        singleGrid = [['A']]
        self.assertTrue(exist(singleGrid, "A"))
        self.assertFalse(exist(singleGrid, "F"))
    
    def testDouble(self):
        twoByTwo = [['A', 'B'], ['C', 'D']]
        self.assertTrue(exist(twoByTwo, "ABDC"))
        self.assertFalse(exist(twoByTwo, "AD"))
        self.assertFalse(exist(twoByTwo, "AAAA"))

    def testTriple(self):
        threeByThree = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        self.assertTrue(exist(threeByThree, "ABCFEDGHI"))
        self.assertFalse(exist(threeByThree, "ABFHD"))
        self.assertFalse(exist(threeByThree, "AAAA"))
        self.assertTrue(exist(threeByThree, "GHEF"))


   

if __name__ == '__main__':
   unittest.main()