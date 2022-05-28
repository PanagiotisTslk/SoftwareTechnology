''' Script for Class Crawler '''


# Libraries


# Class for students
class Crawler:

    # Constructor
    def __init__(self, websites, kind):
        self.websites = websites
        self.kind = kind

    def ActivateCrawler(self):
        pass


# Connection with database
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]


