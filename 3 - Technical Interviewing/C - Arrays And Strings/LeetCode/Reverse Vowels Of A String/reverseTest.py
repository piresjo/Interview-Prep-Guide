import unittest
from reverse import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(reverseVowels("Hello World"), "Hollo Werld")
        self.assertEqual(reverseVowels("asdf"), "asdf")
        self.assertEqual(reverseVowels("qwty"), "qwty")
        self.assertEqual(reverseVowels("AeIoU"), "UoIeA")
        


if __name__ == '__main__':
   unittest.main()