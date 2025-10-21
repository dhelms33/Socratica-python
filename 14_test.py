import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(1), pi)
        self.assertAlmostEqual(0),0)
        self.assertAlmostEqual(2.1), pi * 2.1**2)