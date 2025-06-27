class Choices:
    def __init__(self, u_str):
        self.u_str = u_str
    
    def choices_input(self):
        if len(self.u_str) < 6:
            return("You need a longer string!")
        elif len(self.u_str) > 6:
            return("This string is all right!")
        else:
            return("Wait, what?!")
if __name__ == "__main__":
    try:
        user_input = input("Please input a string to be judged!")
        obj_instance = Choices(user_input)
        result = obj_instance.choices_input()
        print(result)
    except ValueError as ve:
        print(f"Error encountered: " {ve})
    
        
            