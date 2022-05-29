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

    def DownloadNote(self, course, filename):
        # Find Drive folder id for the specific course
        # Connecting with database
        dbname = get_database() 
        # Choosing collection
        col = dbname["Courses"]

        for n in col.find():
            # Retrieve drive folder id from Courses Collection
            if n['name'] == course:
                folder_id = n['driveID']

        # Connection with Google Drive
        drive = drive_connection()

        # Get list of all files inside folder
        file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()

        # Find correct file
        for file in file_list:
            if file["title"] == filename:
                # Download file
                file.GetContentFile(file['title'])

        print("Note downloaded successfully")
        return True
        

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

    def UpdateNote(self, course, notename, newFilename, newDescription, newNotename):
        
        sizeCheck = False

        # Check size of file
        sizeCheck = self.CheckFileSize(newFilename)

        # If file size is ok the proceed with the updates needed
        if sizeCheck is True:

            ''' Get old note filename and update DataBase Note Document '''
            
            # Connecting with database
            dbname = get_database() 
            # Choosing Note collection
            col = dbname["Note"]

            for n in col.find():
                # Retrieve old note filename that will be deleted from Google Drive
                # and old: notename, description and timestamp.
                if n['notename'] == notename:
                    oldNotename = n['notename']
                    oldFilename = n['filename']
                    oldDescr = n['description']
                    oldTimestamp = n['timestamp']
                    
            # Find new timestamp
            timestampNow = datetime.now().strftime('%d-%m-%Y')

            # DataBase update for note notename
            queryNotename = { 'notename': oldNotename } 
            newValues_Notename = { "$set": { "notename": newNotename } }

            # DataBase update for note description
            queryDescr = { 'description': oldDescr }
            newValues_Descr = { "$set": { "description": newDescription } }

            # DataBase update for note timestamp
            queryTimestamp = { 'timestamp': oldTimestamp }
            newValues_Timestamp = { "$set": { "timestamp": timestampNow } }

            # Make the updates
            col.update_one(queryNotename, newValues_Notename)
            col.update_one(queryDescr, newValues_Descr)
            col.update_one(queryTimestamp, newValues_Timestamp)

            ''' Delete old file in Google Drive '''

            # Connecting with database
            dbname = get_database() 
            # Choosing Courses collection
            col = dbname["Courses"]

            for n in col.find():
                # Retrieve drive folder id from Courses Collection
                if n['name'] == course:
                    folder_id = n['driveID']

            # Connection with Google Drive
            drive = drive_connection()

            # Get list of all files inside folder
            file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()

            # Find correct file
            for file in file_list:
                if file["title"] == oldFilename:
                    # Delete file permanently
                    file.Delete()

            ''' Upload new note file in Google Drive '''

            # Select Google Drive folder to upload file
            gfile = drive.CreateFile({'parents': [{'id': folder_id}]})
            # Read file and upload it to folder.
            gfile.SetContentFile(newFilename)
            gfile.Upload()

            print("Note updated successfully!")

        return sizeCheck

    def DeleteNote(self, course, notename, filename):
        # Delete note file from Google Drive
        # Find Drive folder id for the specific course
        # Connecting with database
        dbname = get_database() 
        # Choosing Courses collection
        col = dbname["Courses"]

        for n in col.find():
            # Retrieve drive folder id from Courses Collection
            if n['name'] == course:
                folder_id = n['driveID']

        # Connection with Google Drive
        drive = drive_connection()

        # Get list of all files inside folder
        file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()

        # Find correct file
        for file in file_list:
            if file["title"] == filename:
                # Delete file permanently
                file.Delete()

        # Delete Note from Data Base
        # Choosing Notes collection
        col = dbname["Notes"]
        query = { "notename": notename }

        # Delete note Document
        col.delete_one(query)

        print("Note deleted successfully")
        return True

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
