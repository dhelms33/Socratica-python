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
    fibonacci_cache = {}
    def fib_memo(self.base):
        if self.base == 1:
            return 1
        elif self.base == 2:
            return 1
        elif self.base > 2:
            value = fib_memo(n-1) + fib_memo(n-2)
        fibonacci_cache[self.base] = value
        return value
if __name__ == "__main__":
    try:
        ui = int(input("Please input a base case larger than 2."))
        obj_inst = fibs(ui)
        for n in range(1,ui):
            print(n, ":", fib_memo(ui))
    except ValueError:
        print("This is not an int, try again.")
    