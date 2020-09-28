import unittest
from reverse import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertEqual(reverse(None), "")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("Hello"), "olleH")

if __name__ == '__main__':
   unittest.main()
