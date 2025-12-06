class TestAdder:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def half_adder(self.a, self.b):
        carry = False
        if self.a == 1 and self.b == 1:
            carry = True
            return(0)
        elif self.a == 1 and self.b == 0:
            return(1)
        elif self. a == 0 and self.b == 1:
            return(1)
        else:
            return 0
        