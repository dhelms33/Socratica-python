import logging
class DoomFriends:
    def __init__(self, name, id, message):
        self.name = name
        self.id = id
        self.message = message
        
    def get_doom_logger():
        logging.basicConfig(filename = "E:\\python\\DoomFriends.log", level = logging.DEBUG)
        logger = logging.getLogger()
        return logger.info("First Doom logger message")
    
    def get_doom_err_logger():
        logging.basicConfig(filename="E:\\python\\DoomFriends.log", level = logging.ERROR, format = LOG_FORMAT)
        logger_err = logging.getLogger()
        return logger_err