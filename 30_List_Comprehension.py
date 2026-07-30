import math
#stopped 2:35
class MathyMath:
    def __init__(self, num):
        self.num = num
    
    def create_squares(num):
        squares = []
        if num < 1:
            return("Error! Please try a number greater than 1")
        for item in range(1, num):
            squares.append(i**2)
        return squares
    
    def create_simple_sq(num):
        if num < 1:
            return("Error! Please try a number greater than 1")
        squares2 = [i**2 for i in range(1, num)]
        return squares2
    #left off 2:16
    
    def squares_in_list(num):
        squares = []
        if type(num) == str:
            raise TypeError("This is not the correct type. Try an int, double, or float.")
        for i in range(1, num):
            squares.append(i**2)
        return squares
    
    def squares_list_comp(num):
        squares_comp = [i**2 for i in range(1,num)]
        return squares_comp
    
    def mod_5(num):
        remainders_5 = [x**2 % 5 for x in range(1,num)]
        return remainders_5
        