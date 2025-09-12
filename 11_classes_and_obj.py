#left off 3:37
#make a class that does nothing
class User:
    pass

if __name__ == "__main__":
    user1 = User()
    #user1 is an instance or object 
    user1.first_name = "Dave"
    user1.last_name = "Boogeyman"
    #these are fields
    print(user1.first_name)
    print(user1.last_name)
    
    #stand alone variables are not attached or associated with user1
    first_name = "Arthur"
    last_name = "Clarke"
    
    #values kept seperate
    user2 = User()
    user2.first_name = "Frank"
    user2.last_name = "Poop"
    
    #discrepancy in fields
    user1.age = 37
    user2.favorite_book = "2001: A Space Odyssey"
    
    