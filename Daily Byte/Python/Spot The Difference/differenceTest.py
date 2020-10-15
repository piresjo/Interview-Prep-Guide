import unittest
from difference import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(difference("foobar", "barfoot"), 't')
        self.assertEqual(difference("ide", "idea"), 'a')
        self.assertEqual(difference("coding", "ingcod"), '')
        

if __name__ == '__main__':
   unittest.main()
