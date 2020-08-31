import unittest
from findProfession import *

class Test(unittest.TestCase):
    
    def testWithBase(self):
       self.assertEqual(findProfession(1, 1), "Engineer")

    def testOnLevel2(self):
       self.assertEqual(findProfession(2, 2), "Doctor")

    def testOnLevel3(self):
       self.assertEqual(findProfession(3, 3), "Doctor")
    
    def testAdvanced(self):
        self.assertEqual(findProfession(25, 16777216), "Engineer")
      

if __name__ == '__main__':
   unittest.main()
