import unittest
from firstNonRepeatingCharacter import *

class Test(unittest.TestCase):
    
    def testWithEmptyString(self):
        self.assertEqual(firstNotRepeatingCharacter(""), "_")

    def testWithSingleString(self):
        self.assertEqual(firstNotRepeatingCharacter("a"), "a")

    def testWithNoNonRepeating(self):
        self.assertEqual(firstNotRepeatingCharacter("aassddff"), "_")

    def testWithNonRepeating(self):
        self.assertEqual(firstNotRepeatingCharacter("aassdff"), "d")
      

if __name__ == '__main__':
   unittest.main()
