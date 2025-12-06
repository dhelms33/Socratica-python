import unittest
from 23_TestAdder import half_adder
class TestAdder:
    def test__area(unittest.TestCase):
        self.assertAlmostEqual(half_adder(1,1), carry = True, 0)
        self.assertAlmostEqual(half_adder(1,0), carry = False, 1)