#left off 7:17
class User:
    """ Member of friend face. Only stores first and last names and birthday."""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        
    def extract_names(self):
        #Extract first and last names
        name_pieces = self.name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1] #let this be the last thing they entered
        return self.first_name + self.last_name
    
if __name__ == "__main__":
    user = User("Dave Bowman", 19710317)
    #print(user.name)
    print(user.first_name)
    print(user.last_name)
    print(user.birthday)
    
        