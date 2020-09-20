import unittest
from patterns import *

class Test(unittest.TestCase):
    def test(self):
        stringsA = ["cat", "dog", "dog"]
        patternsA = ["a", "b", "b"]
        stringsB = ["re", "jjinh", "rnz", "frok", "frok", "hxytef", "hxytef", "frok"]
        patternsB = ["kzfzmjwe", "fgbugiomo", "ocuijka", "gafdrts", "gafdrts", "ebdva", "ebdva", "gafdrts"]
        stringsC = ["cat", "dog", "doggy"]
        patternsC = ["a", "b", "b"]

        self.assertTrue(areFollowingPatterns(stringsA, patternsA))
        self.assertTrue(areFollowingPatterns(stringsB, patternsB))
        self.assertFalse(areFollowingPatterns(stringsC, patternsC))

if __name__ == '__main__':
   unittest.main()