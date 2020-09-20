import unittest
from amend import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertEqual(amendTheSentence(None), "")
        self.assertEqual(amendTheSentence(""), "")
        self.assertEqual(amendTheSentence("CodesignalIsAwesome"), "codesignal is awesome")
        self.assertEqual(amendTheSentence("tfRZGdYurvrVyEuHbOJcaXnZrsEUr"), "tf r z gd yurvr vy eu hb o jca xn zrs e ur")
        self.assertEqual(amendTheSentence("Hello"), "hello")

if __name__ == '__main__':
   unittest.main()
