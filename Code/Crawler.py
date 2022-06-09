""" Script for Class Crawler """


# Libraries


# Class for students
class Crawler:

    # Constructor
    def __init__(self, url, title, body, author):
        self.url = url
        self.title = title
        self.body = body
        self.author = author

    def ActivateCrawler(self):
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
            print(f"Url of announcement {i+1} is {content_list[i]['url']}")


# Connection with database
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]
