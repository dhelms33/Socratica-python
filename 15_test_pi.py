# to run python tests
#python -m unit test test_circles
# python -m unittest
#automatically finds py tests

def circle_area(r):
    return pi(r**2)

#test function 
radii =[2, 0, -3, 2+5j, True, "radius"]
message = "Area of circles with {radius} is {area}." 

for r in radii:
    A = circle_area(r)
    print (message.format(radius=r, area=A))

