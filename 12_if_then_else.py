class Collector:
    def __init__(self, ui, int):
        self.ui = ui
        self.int = int
    
    def length_test(self):
        too_short = False
        if self.ui < 6:
            too_short = True
            return("This string is too short")
        else: 
            return("This string is fine")
    def even_or_odd(self):
        is_even = False
        if self.int % 2 == 0:
            is_even = True
            return ("This number is even")
        else:
            return("This number is odd.")
        
if __name__ == "__main__":
    user_input = input("Please enter a string")
    user_input_int = int(input("Please enter an int"))
    obj_inst_str = Collector
    obj_inst_str.length_test(user_input)
    obj_inst_int = Collector
    obj_inst_int.even_or_odd(user_input_int)
    
    