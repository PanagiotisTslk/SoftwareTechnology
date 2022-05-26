''' Script for Class Course '''

# Libraries


# Class for courses
class Course:

    # Constructor
    def __init__(self, name, semester, academy, professor, ECTS, points, kind):
        self.name = name
        self.semester = semester
        self.academy = academy
        self.professor = professor
        self.ECTS = ECTS
        self.points = points
        self.kind = kind

    # Retrieving the course that selected from student
    def RetrieveCourseInfo(self):

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Courses"]

        for c in col.find():
            if c['name'] == self.name:
                print(c)
                self.semester = c['semester']
                self.academy = c['academy']
                self.professor = c['professor']
                self.ECTS = c['ECTS']
                self.points = c['points']
                self.kind = c['kind']


# Connection with database
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://****:************@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]
