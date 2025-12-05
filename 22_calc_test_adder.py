import unittest
class TestAdder:
    def __init__(self,a,b,input):
        self.assertAlmostEqual(carry_adder(a,b), 1,1)
        self.b = b
    def test_