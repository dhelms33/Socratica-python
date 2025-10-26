import unittest
from test_pi import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(1), pi)
        self.assertAlmostEqual(0),0)
        self.assertAlmostEqual(2.1), pi * 2.1**2)
    
    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)
    
    def test_types(self):
        #Make sure type errors are raised
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "String")
        
        
        