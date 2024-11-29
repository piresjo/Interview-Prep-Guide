import unittest
from uncommon import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(uncommon("the quick", "brown fox"), ["the", "quick", "brown", "fox"])
        self.assertEqual(uncommon("the tortoise beat the haire", "the tortoise lost to the haire"), ["beat", "lost", "to"])
        self.assertEqual(uncommon("copper coffee pot", "hot coffee pot"), ["copper", "hot"])

if __name__ == '__main__':
   unittest.main()
