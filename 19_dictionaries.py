#pass
class SpiffoFriendNetwork:
    post_og = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English", "datetime":"20230317","location":(44.590533, -104.715556)}

    def __init__(self, user_id):
        self.user_id = user_id
        
    def get_post():
        post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English", "datetime":"20230317","location":(44.590533, -104.715556)}
        return post
#type(post)
#creating a new post using the dict constructor
    def get_post2():
        post2 = dict(message="SS Cotopaxi", language="English")
        return post2
    def get_post3 (self.user_id, message):
        post3 = dict(id = self.user_id, msg = message)
        return post3
    def get_location_dict(self.user_id, location):
        location_dict = dict(id = self.user_id, loc = location)
        return location_dict
    def get_userid():
        u_id_post_og = post_og["user_id"]
        return u_id_post_og
    def loop_dictionary():
        for item in range(len(post_og)):
            if 'location' in post_og:
                return post_og['location']
            else: 
                error_message = "location not in post_og"
        return error_message
                
        
    
    
