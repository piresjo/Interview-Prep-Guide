import unittest
from score import *

class Test(unittest.TestCase):
    
    def testWithNone(self):
        self.assertEqual(scoreOfParentheses(None), 0)
        self.assertEqual(scoreOfParentheses(""), 0)
    
    def testGeneral(self):
        self.assertEqual(scoreOfParentheses("()"), 1)
        self.assertEqual(scoreOfParentheses("()()"), 2)
        self.assertEqual(scoreOfParentheses("(())"), 2)
        self.assertEqual(scoreOfParentheses("(()())"), 4)


      

if __name__ == '__main__':
   unittest.main()
