import unittest
from merge import *

class Test(unittest.TestCase):
    
    def testWithBaseCases(self):
       self.assertEqual(merge(None, None, 0, 0), None)
       self.assertEqual(merge([2], None, 0, 0), [2])

    def testGeneralCase(self):
        self.assertEqual(merge([1, 4, 5, 8, 10], [], 5, 0), [1, 4, 5, 8, 10])
        self.assertEqual(merge([1, 4, 5, 8, 10, 0, 0], [3, 9], 5, 2), [1, 3, 4, 5, 8, 9, 10])

      

if __name__ == '__main__':
   unittest.main()