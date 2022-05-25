''' Script for Class Evluation '''

# Libraries
from datetime import datetime

# Class for evaluations
class Evaluation:

    # Constructor
    def __init__(self, evaluator, rate, comments, timestamp):
        self.evaluator = evaluator
        self.rate = rate
        self.timestamp = timestamp

    # Making an evaluation (Calls CheckGrade() and StoreEvalution())
    def MakeEvaluation(self, evaluator, rate, comments):

        isMade = False

        check = self.CheckGrade(rate)
        if check == True:

            self.rate = rate
            self.evalutor = evaluator

            if comments is not None:
                self.comments = comments

            else:
                self.comments = ''

            self.timestamp = datetime.now()
            print('Here calls StoreEvalution()!\n')
            isMade = True

        else:
            isMade = False
            print('Here returns to screen to complete the form again!\n')

        return isMade

    def CheckGrade(self, grade):

        isValid = True

        if grade >= 0 and grade <= 5:
            isValid = True

        else:
            isValid = False
            print('Grade has invalid value!\n')

        return isValid

    # Taking an evaluation object and storing it to database
    def StoreEvaluation(self, course):

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Evaluations"]

        evaluation = {
            "course": course,
            "evaluator": self.evaluator,
            "rate": self.rate,
            "comments": self.comments,
            "timestamp": datetime.now()
        }

        col.insert_one(evaluation)
        print("Evaluation created successfully")

    # Retrieving all evaluations of a course given
    def RetrieveEvaluations(self):

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Evaluations"]

        for c in col.find():
            if c['course'] == self.course:
                print(c)
                self.evaluator = c['evaluator']
                self.rate = c['rate']
                self.comments = c['comments']
                self.timestamp = c['timestamp']


# Connection with database
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://tslk:Tslkgtx950pt@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]