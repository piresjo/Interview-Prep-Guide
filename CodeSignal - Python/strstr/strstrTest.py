import unittest
from strstr import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertEqual(strStr("CodefightsIsAwesome", "IA"), -1)
        self.assertEqual(strStr("CodefightsIsAwesome", "IsA"), 10)
        self.assertEqual(strStr("a", "a"), 0)
        self.assertEqual(strStr("a", "A"), -1)

if __name__ == '__main__':
   unittest.main()
