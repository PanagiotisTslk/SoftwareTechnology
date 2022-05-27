''' Script for Class Announcement '''

# Libraries
from datetime import datetime
import Crawler.py


# Class for evaluations
class Announcement:

    # Constructor
    def __init__(self, timestamp, author, text, website, kind):
        self.timestamp = timestamp
        self.author = author
        self.text = text
        self.website = website
        self.kind = kind

    # Taking an evaluation object and storing it to database
    def StoreAnnouncements(self, website):

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Announcements"]

        announcement = {
            "author": self.author,
            "text": self.text,
            "website": website,
            "kind": self.kind,
            "timestamp": datetime.now()
        }

        col.insert_one(announcement)
        print("Announcement stored successfully")

    # Retrieving all evaluations of a course given
    def RetrieveEvaluations(self):

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Announcements"]

        for c in col.find():
            if c['website'] == self.website:
                self.author = c['author']
                self.text = c['text']
                self.website = c['website']
                self.kind = c['kind']
                self.timestamp = c['timestamp']

    def ReclassifyAnnouncements(self):
        pass

    def CheckSourceAnnouncements(self):
        pass

    def LoadPage(self):
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
