import unittest
from reorg import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(reorganizeString('aab'), 'aba')
        


if __name__ == '__main__':
   unittest.main()
