#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class Evaluation '''

# Libraries
from datetime import datetime

# Class for evaluations
class Evaluation:

    # Constructor
    def __init__(self, evaluator, course, rate, comments, timestamp):
        self.evaluator = evaluator
        self.course = course
        self.rate = rate
        self.comments = comments
        self.timestamp = timestamp

    # Making an evaluation (Calls CheckGrade() and StoreEvalution())
    def MakeEvaluation(self, rate, comments):

        isMade = False

        check = self.CheckGrade(rate)

        if check == True:

            if comments is not None:
                self.comments = comments

            else:
                self.comments = ''

            self.timestamp = datetime.now().strftime('%d-%m-%Y')
            print('Here calls StoreEvalution()!\n')
            isMade = True

        else:
            isMade = False
            print('Here returns to screen to complete the form again!\n')

        return isMade


    # Cheking if grades has valid value
    def CheckGrade(self, grade):

        isValid = True

        if grade >= 0 and grade <= 5:
            isValid = True

        else:
            isValid = False
            print('Grade has invalid value!\n')

        return isValid

    # Taking an evaluation object and storing it to database
    def StoreEvaluation(self):

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Evaluations"]

        evaluation = {
            "course": self.course,
            "evaluator": self.evaluator,
            "rate": self.rate,
            "comments": self.comments,
            "timestamp": datetime.now().strftime('%d-%m-%Y')
        }

        col.insert_one(evaluation)
        print("Evaluation created successfully!")

    # Retrieving all evaluations of a course given
    def RetrieveEvaluations(self):

        # List with notes to be returned
        evaluations_list = []

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Evaluations"]

        for c in col.find():

            if c['course'] == self.course:

                evaluation = {
                    "course": c['course'],
                    "evaluator": c['evaluator'],
                    "rate": c['rate'],
                    "comments": c['comments'],
                    "timestamp": c['timestamp']
                }
                evaluations_list.append(evaluation)

        return evaluations_list


# Connection with database
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://tslk:Tslkgtx950pt@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]
