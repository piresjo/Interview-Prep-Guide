import unittest
from stackMin import *

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minimumOnStack(["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]), [10, 5, 5, 5, 10])
        self.assertEqual(minimumOnStack([]), [])
        self.assertEqual(minimumOnStack(["push 10"]), [])
        self.assertEqual(minimumOnStack(["min"]), [])
        self.assertEqual(minimumOnStack(["pop"]), [])

if __name__ == '__main__':
   unittest.main()