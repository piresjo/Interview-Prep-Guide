import unittest
from duplicates import *

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(containsDuplicates(None))
        self.assertFalse(containsDuplicates([]))
        self.assertTrue(containsDuplicates([1, 1, 2, 3, 4]))
        self.assertFalse(containsDuplicates([1, 2, 3, 4]))


if __name__ == '__main__':
   unittest.main()