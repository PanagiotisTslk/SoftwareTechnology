''' Script for Class Announcement '''

# Libraries
import Crawler


# Class for evaluations
class Announcement:

    # Constructor
    def __init__(self, title, author, body, url):
        self.title = title
        self.author = author
        self.body = body
        self.url = url

    # Taking an announcement object and storing it to database
    def StoreAnnouncements(self):

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Announcements"]

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
        announcements = soup.find_all('a', {"class": "_self"})

        # List that contains url for announcements pages
        url_list = []

        # Extract urls for announcements pages
        for url in announcements:
            url_list.append(url.get("href"))

        ##--- Extract Content from Urls ---##

        for url in url_list:
            # Take the contents of a page
            with urllib.request.urlopen(url) as response:
                html = response.read()

            # Take page contents with beautifulsoup
            soup = BeautifulSoup(html, features="html.parser")

            # Extract text from specific html tags
            # Get Announcement: 1.Title, 2.Body, 3.Author
            html_title = soup.find_all('h1', {'class': 'entry-title'})  # Title
            html_body = soup.find_all('div', {'class': 'entry-content'})  # Body
            html_author = soup.find_all('a', {'class': 'url fn n'})  # Author

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

        # Parse specific contents of announcement
        # Store announcements in database

            announcement = {
                "author": author,
                "body": body,
                "url": url,
                "title": title
            }

            col.insert_one(announcement)
            print("Announcement stored successfully")

    # Retrieving all announcements
    def RetrieveAnnouncements(self):
        aCrawler = Crawler.Crawler('', '', '', '')
        aCrawler.ActivateCrawler()
        print('\n')

    def ReclassifyAnnouncements(self, author_called):
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
        announcements = soup.find_all('a', {"class": "_self"})

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
            html_title = soup.find_all('h1', {'class': 'entry-title'})  # Title
            html_body = soup.find_all('div', {'class': 'entry-content'})  # Body
            html_author = soup.find_all('a', {'class': 'url fn n'})  # Author

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

            if author_called == author:
                contents = {
                    "title": title,
                    "body": body,
                    "author": author,
                    "url": url
                }

                content_list.append(contents)

        # Parse specific contents of content_list
        # Get urls from announcements

        for i in range(0, len(content_list)):
            print(f"Url of announcement with author {content_list[i]['author']} is {content_list[i]['url']}")
        print('\n')


# Connection with database
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]


aAnnouncement = Announcement('', '', '', '')
aAnnouncement.RetrieveAnnouncements()
aAnnouncement.ReclassifyAnnouncements('admin')
aAnnouncement.StoreAnnouncements()
