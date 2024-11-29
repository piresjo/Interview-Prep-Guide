import unittest
from firstDuplicate import *

class Test(unittest.TestCase):

   def testWithNone(self):
      self.assertEqual(firstDuplicate(None), -1)

   def testWithEmptyList(self):
      self.assertEqual(firstDuplicate([]), -1)

   def testWithSingleList(self):
      self.assertEqual(firstDuplicate([1]), -1)

   def testWithDoubleListNoDuplicate(self):
      self.assertEqual(firstDuplicate([1, 2]), -1)

   def testWithDoubleListDuplicate(self):
      self.assertEqual(firstDuplicate([1, 1]), 1)

   def testWithLongListNoDuplicate(self):
      listVal = [1, 2, 3, 4, 5, 6, 7]
      self.assertEqual(firstDuplicate(listVal), -1)

   def testWithLongListDuplicate(self):
      listVal = [1, 2, 3, 4, 2, 3, 4]
      self.assertEqual(firstDuplicate(listVal), 2)

if __name__ == '__main__':
   unittest.main()
