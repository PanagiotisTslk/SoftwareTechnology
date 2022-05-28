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
    def RetrieveAnnouncements(self):

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


### Crawling Process ###

import urllib.request
from bs4 import BeautifulSoup

##--- Extract Links ---## 

# Upatras url page
upatras = "https://www.upatras.gr/category/news/"

# Take the contents of a page
with urllib.request.urlopen(upatras) as response:
	   html = response.read()

# Take page contents with beautifulsoup
soup = BeautifulSoup(html, features="html.parser")

# Get specific tag from html page
announcements = soup.find_all('a', {"class":"_self"})

# List that contains url for announcements pages
url_list = []

# Extract urls for announcements pages
for url in announcements:
    url_list.append(url.get("href"))

##--- Extract Content from Urls ---##

# List with dictionaries that contain 1.Title, 2.Body, 3.Author, 4.url of announcement
content_list = []
    
for url in url_list:
    # Take the contents of a page
    with urllib.request.urlopen(url) as response:
        html = response.read()

    # Take page contents with beautifulsoup
    soup = BeautifulSoup(html, features="html.parser")

    # Extract text from specific html tags
    # Get Announcement: 1.Title, 2.Body, 3.Author
    html_title = soup.find_all('h1', {'class':'entry-title'}) # Title
    html_body = soup.find_all('div', {'class':'entry-content'}) # Body
    html_author = soup.find_all('a', {'class':'url fn n'})  # Author

    title = ""
    body = ""
    author = ""

    # Take only the text without html tags and metadata
    for content in html_title:
        title = content.text

    for content in html_body:
        body += content.text + " "

    for content in html_author:
        author = content.text

    contents = {
        "title": title,
        "body": body,
        "author": author,
        "url": url
    }

    content_list.append(contents)



# Parse specific contents of content_list
# Get title from 2nd announcement
content_list[1]["title"]


