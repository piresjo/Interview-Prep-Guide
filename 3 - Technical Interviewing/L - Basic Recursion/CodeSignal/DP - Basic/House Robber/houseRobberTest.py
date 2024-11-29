import unittest
from houseRobber import *

class Test(unittest.TestCase):

    def testWithEdgeCases(self):
        self.assertEqual(houseRobber(None), 0)
        self.assertEqual(houseRobber([]), 0)
        self.assertEqual(houseRobber([1]), 1)
        self.assertEqual(houseRobber([1, 4]), 4)

    def testGeneralCases(self):
        self.assertEqual(houseRobber([1, 1, 1]), 2)
        self.assertEqual(houseRobber([1, 2, 1, 0]), 2)
        self.assertEqual(houseRobber([55, 72, 209, 143, 216, 220, 122, 115, 87, 227, 220, 161, 79, 230, 55, 56, 56, 178, 124, 88, 202, 65, 102]), 1758)

    

        
       
if __name__ == '__main__':
   unittest.main()