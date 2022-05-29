#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class Note '''

# Libraries
from datetime import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path

# Class for Note
class Note:

    # Constructor
    def __init__(self, notename, filename, course, timestamp, description, author):
        self.notename = notename
        self.filename = filename
        self.course = course
        self.timestamp = timestamp
        self.description = description
        self.author = author

    def SearchNote(self):
        # List with note names to be returned
        notes_list = []

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Notes"]

        for n in col.find():
            # Check only notes from the selected course
            if n['course'] == self.course:
                notes_list.append(n['notename'])

        return notes_list

    def DownloadNote(self):
        # Connectiong with Google Drive
        drive = drive_connection()
        

    def CheckFileSize(self, upfile):
        isRight = False

        # Get Path of the file
        file = Path(upfile)
        # Get size of the file
        fileSize = file.stat().st_size

        # Check if file size is more than 100 MB = 104857600 Bytes
        if fileSize > 104857600:
          isRight = False
        else:
          isRight = True

        return isRight

    def StoreNote(self, file):
        
        sizeCheck = False
        
        # Uploading file in Drive
        # Find Drive folder id for the specific course
        # Connecting with database
        dbname = get_database() 
        # Choosing collection
        col = dbname["Courses"]

        for n in col.find():
            # Retrieve drive folder id from Courses Collection
            if n['name'] == self.course:
                folder_id = n['driveID']

        # Connectiong with Google Drive
        drive = drive_connection()

        # Check size of file
        sizeCheck = self.CheckFileSize(self.filename)

        if sizeCheck is True:
            # Select Google Drive folder to upload file
            gfile = drive.CreateFile({'parents': [{'id': folder_id}]})
            # Read file and upload it to folder.
            gfile.SetContentFile(self.filename)
            gfile.Upload()
            
            # Connecting with database
            dbname = get_database()
            # Choosing collection
            col = dbname["Notes"]

            note = {
                "natename": self.notename,
                "filename": self.filename,
                "course": self.course,
                "description": self.description,
                "author": self.author,
                "timestamp": self.timestamp
            }

            col.insert_one(note)
            print("Note stored successfully!")
            
        return sizeCheck

    def RetrieveNote(self):

        # List with notes to be returned
        notes_list = []

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Notes"]

        for n in col.find():
            # Check only notes from the selected course
            if n['course'] == self.course:

                note = {
                    "natename": n['notename'],
                    "filename": n['filename'],
                    "course": n['course'],
                    "description": n['description'],
                    "author": n['author'],
                    "timestamp": n['timestamp']
                }
                notes_list.append(note)

        return notes_list

    def UpdateNote(self):
        pass

    def DeleteNote(self):
        pass

    # SAKIS
    def CheckDownloadedNotes(self):
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

# Connection with Google Drive Storage
def drive_connection():

    # Class for oauth2client library in google-api-python-client
    gauth = GoogleAuth("credentials.txt")

    # Load credentials file
    gauth.LoadCredentialsFile(self.credsFile)

    # Check credentials
    if gauth.credentials is None:
        return False
    else:
        # Initialize the credentials
        gauth.Authorize()
        drive = GoogleDrive(gauth) 

    return drive


# # MENU
#
# # User's inputs
# name = "Data_Mining-sos"
# description = "This file contains sos for Data Mining course"
# file = "Data_Mining-sos.zip"
#
# # System data (from previous menus)
# user = 'andrew97'
# timestamp = datetime.now().strftime('%d-%m-%Y')
# course = "Data Mining"
#
# aNote = Note(name, course, timestamp, description, user, [])
#
# notes = aNote.RetrieveNote()
#
# notes_list = []  # List with all note objects
#
# for x in range(len(notes)):
#
#     filename = notes[x]['filename']
#     course = notes[x]['course']
#     timestamp = notes[x]['timestamp']
#     description = notes[x]['description']
#     author = notes[x]['author']
#     comments = notes[x]['comments']
#
#     notes_list.append(Note(filename, course, timestamp, description, author, comments))
#
# for x in notes_list:
#     print(x.filename)
