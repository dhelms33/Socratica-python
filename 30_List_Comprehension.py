class MathyMath:
    def __init__(self, num):
        self.num = num
    
    def create_squares(num):
        squares = []
        if num > 1:
            return("Error! Please try a number greater than 1")
        for item in range(1, num):
            squares.append(i**2)
        return squares
    
    def create_simple_sq(num):
        squares2 = [i**2 for i in range(1, num)]
        return squares2
    #left off 2:16