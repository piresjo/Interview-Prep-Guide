import unittest
from firstUnique import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertEqual(firstUniqChar("abcabd"), 2)
        self.assertEqual(firstUniqChar("thedailybyte"), 1)
        self.assertEqual(firstUniqChar("developer"), 0)
        self.assertEqual(firstUniqChar("aassddff"), -1)

if __name__ == '__main__':
   unittest.main()
