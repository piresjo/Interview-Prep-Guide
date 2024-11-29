import unittest	
from nextGreater import *	

class TestStringMethods(unittest.TestCase):		

    def testGeneral(self):	
        self.assertEqual(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1,3,-1])
        				


if __name__ == '__main__':	
   unittest.main()