#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class Note '''

# Libraries
from datetime import datetime


# Class for Note
class Note:

    # Constructor
    def __init__(self, filename, course, timestamp, description, author):
        self.filename = filename
        self.course = course
        self.timestamp = timestamp
        self.description = description
        self.author = author

    def SearchNote(self):
        pass

    def DownloadNote(self):
        pass

    def CheckFileSize(self):
        pass

    def StoreNote(self, file):

        # Uploading file in Drive


        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Notes"]

        note = {
            "filename": self.filename,
            "course": self.course,
            "description": self.description,
            "author": self.author,
            "timestamp": self.timestamp
        }

        col.insert_one(note)
        print("Note stored successfully!")

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
