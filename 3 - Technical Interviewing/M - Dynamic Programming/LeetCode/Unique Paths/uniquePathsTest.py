import unittest
from uniquePaths import *

class Test(unittest.TestCase):
    
    def testWithBaseCases(self):
       self.assertEqual(uniquePaths(0, 0), 0)
       self.assertEqual(uniquePaths(1, 1), 1)

    def testGeneral(self):
        self.assertEqual(uniquePaths(3, 2), 3)
        self.assertEqual(uniquePaths(7, 3), 28)

      

if __name__ == '__main__':
   unittest.main()
