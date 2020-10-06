import unittest
from defang import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertEqual(defangIPaddr(""), "")
        self.assertEqual(defangIPaddr("hello"), "hello")
        self.assertEqual(defangIPaddr("1.1.1.1"), "1[.]1[.]1[.]1")
        self.assertEqual(defangIPaddr("121.121.121.121"), "121[.]121[.]121[.]121")

if __name__ == '__main__':
   unittest.main()