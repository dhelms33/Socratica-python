import math
#left off 2:22
def area(r):
    return math.pi * (r**2)

#method 1: direct

areas = [] 
for r in radii:
    a = area(r)
    areas.append(a)
    
#method 2 map
map_object = map(area, radii)
list_map = list((map_object))