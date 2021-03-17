import unittest

from functions import *

class Tests(unittest.TestCase):

    def test_1(self):
        """ Ensure 'square' works properly """
        self.assertEqual(square(5), 25)
    
    def test_2(self):
        """ Ensure 'double' works properly """
        self.assertEqual(double(6), 12)
    
    def test_3(self):
        """ Ensure 'triple' works properly """
        self.assertEqual(triple(6), 18)

if __name__ == "__main__":
    unittest.main()