#Logging allows us to determine the cause by writing status messages to a file or other streams
#Five built in levels: Debug, Info, Warning, Error, Critical

#Stopped at 3:22

import logging
#allows us to look inside of module
dir(logging)
class Logging_Socratica:
    #create and configure logger
    logging.basicConfig(filename = "E:\\python\\Lumberjack.Log", level = logging.DEBUG) #basicconfig sets level to 30
    #if file does not exist python will create it
    
    logger = logging.getLogger()
    #working with one logger without a name. Known as root logger.
    
    #Test the logger
    logger.info("Our first info message.")
    
    print(logger.level)
    
    #There are six preset levels
    #NotSet 0
    #DEBUG 10
    #INFO 20
    #WARNING 30
    #ERROR 40
    #CRITICAL 50
    
    if __name__ == __main__:
        new_logging = Logging_Socratica()
        print(new_logging)