import unittest
from simplify import *

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(simplifyPath("/home/a/./x/../b//c/"), "/home/a/b/c")
        self.assertEqual(simplifyPath("/a/b/c/../.."), "/a")
        self.assertEqual(simplifyPath("/../"), "/")
        self.assertEqual(simplifyPath("/"), "/")
        self.assertEqual(simplifyPath("a/b/../c/d/../../e/../../"), "/")
        self.assertEqual(simplifyPath("/cHj/T//"), "/cHj/T")

if __name__ == '__main__':
   unittest.main()