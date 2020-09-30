import unittest
from product import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertEqual(productExceptSelf([1, 2, 3, 4]), [24,12,8,6])

if __name__ == '__main__':
   unittest.main()