#Logging allows us to determine the cause by writing status messages to a file or other streams
#Five built in levels: Debug, Info, Warning, Error, Critical

#Stopped at 4:37

import logging
#allows us to look inside of module
dir(logging)
class LoggingLumberjack:
    def __init__(self):
    #create and configure logger
        self.logging.basicConfig(filename = "C:\\python\\Lumberjack.Log", 
                                 level = logging.DEBUG) #basicconfig sets level to 30
    #if file does not exist python will create it
    
        self.logger = logging.getLogger()
    #working with one logger without a name. Known as root logger.
    
    #Test the logger
        self.logger.info("Our first info message.")
        self.logger.info("Our second message")
    
        print(logger.level)
    
    #There are six preset levels
    #NotSet 0
    #DEBUG 10
    #INFO 20
    #WARNING 30
    #ERROR 40
    #CRITICAL 50
    
    #need to input the time that the log was created
    
    class EnragedLumber:
        def __init__(self):
            self.LOG_FORMAT= "%(levelname)s %asctime)s - %(message)"
            self.logging.basicConfig(filename = "C:\\python\\EnragedLumberjack.Log", 
                            level = logging.DEBUG, 
                            format = LOG_FORMAT,
                            filemode = 'w')
            logger = self.logging.getLogger()
            #Test the logger
            self.logger.info("Our SECOND message in Enraged Lumber")
    
    if __name__ == "__main__":
        new_logging_lumber = LoggingLumberjack()
        new_logging_enraged = EnragedLumber()
        print("Logging intialized for both classes")