# to run python tests
#python -m unit test test_circles
# python -m unittest
#automatically finds py tests
from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The raidus must be a non-negative real number")
    if r < 0:
        raise ValueError("Value cannot be negative.")
    return pi*(r**2)

#test function 
radii =[2, 0, -3, 2+5j, True, "radius"]
message = "Area of circles with {radius} is {area}." 

for r in radii:
    A = circle_area(r)
    print (message.format(radius=r, area=A))

#look at help text to learn python
import unittest
help(unittest.TestCase.assertSetEqual)


