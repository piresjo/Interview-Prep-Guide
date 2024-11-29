import unittest
from reverse import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertEqual(reverseVowels(""), "")
        self.assertEqual(reverseVowels("hello"), "holle")
        self.assertEqual(reverseVowels("1.1.1.1"), "1.1.1.1")

if __name__ == '__main__':
   unittest.main()