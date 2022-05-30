#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class Admin '''

# Class for Admins
class Admin:

  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def SendErrorLog(self, file):

    # Connecting with database
    dbname = get_database()
    # Choosing collection
    col = dbname["Errors"]

    error = file

    col.insert_one(error)
    print("An error occurred!")


# Connection with database
def get_database():
  # Provide the mongodb atlas url to connect python to mongodb using pymongo
  CONNECTION_STRING = "mongodb+srv://tslk:Tslkgtx950pt@cluster0.jnvsh.mongodb.net/StudentUp"

  # Create a connection using MongoClient
  from pymongo import MongoClient
  client = MongoClient(CONNECTION_STRING)

  # Create the database
  return client["StudentUp"]
