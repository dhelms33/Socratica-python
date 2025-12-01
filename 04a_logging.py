import logging
class DoomFriends:
    def __init__(self, name, id, message):
        self.name = name
        self.id = id
        self.message = message
    def get_doom_logger():
        logging.basicConfig(filename = "E:\\python\\DoomFriends.log")
        logger = logging.getLogger()
        return logger.info("First Doom logger message")