class fibs:
    def init(self, base):
        self.base = base
    
    def fib_og(self.base):
        if self.base ==1:
            return 1
        elif self.base == 2:
            return 1
        elif self.base > 2:
            return(fib_og(self.base-1) + fib_og(self.base-2))