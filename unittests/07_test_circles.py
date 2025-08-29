import unnittest
from 07_circles import calc_area
class TestsCircleArea(unnittest.TestCase):
    def test_area(self):
        #test areas when raidus >= 0
        self.assertAlmostEqual(calc_area(1), pi)
        self.assertAlmostEqual(calc_area(0), 0)
        self.assertAlmostEqual(calc_area(2.1), pi* 2.1**2)
        #not sure if correct
        self.assertRaises(calc_area(-2), ValueError)
        
    def test_values(self):
        #Make sure value errors are raised when necessary
        self.assertRaises(ValueError, calc_area, -2)
#if you want to learn morea bout py, use help text in interative mode
# import unittest
help(unittest.TestCase.assertSetEqual)
    def test_types(self):
        self.assert(TypeError, calc_area, 3+5j)
        self.assert(TypeError, calc_area, True)
        self.assert(TypeError, calc_area, "radius")