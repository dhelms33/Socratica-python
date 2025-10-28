import 
class LearningExceptions:
    def correct_loop(num):
        try:
            #runs first
            for i in range(num):
                #incorrect for i in range(5)
                return("Hello World!")
        except:
            #runs if exception occurs in try block
            ValueError("Please input a number into the loop!")
        finally:
            #this code always executes
            return("Congratulates, you input something correct into the loop!")
    
    def read_file_timed(path):
        #6:29, go back and watch