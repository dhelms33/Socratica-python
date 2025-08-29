from math import pi

""""""
def calc_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError*===("The radius cannot be negative.")
    return pi*(r**2)

#test function
radii = [2,0,-3,2+5j, True, "radius"]
message = "Area of circles with r = {radius} is {area}"
#in python j = sqrt(-1)
for r in radii:
    A = calc_pi(r)
    print(message.format(raidus=r, area = A))
    