# Connection with database
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://tslk:Tslkgtx950pt@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]


# Connecting with database
dbname1 = get_database()
# Choosing collection
col1 = dbname1["Markers"]

academy = {
            "name": ['ceid', 'mhx'],
            "address": ["Panepistimiou 5", "Panepistimiou 10"],
            "num_of_students": [3045, 2190],
            "num_of_professors": [23, 17],
            "inner_map": ["ceid_inner_map", "mhx_inner_map"],
        }

col1.insert_one(academy)
print("Academies created successfully!")


# Class for academies
class Academy:
    # Constructor
    def __init__(self, name, address, num_of_students, num_of_professors, inner_map):
        self.name = name
        self.address = address
        self.num_of_students = num_of_students
        self.num_of_professors = num_of_professors
        self.inner_map = inner_map

    def CheckIfAcademyBuild(self):
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Academy"]

        markers_list = []

        for marker in markers_list:
            for c in col.find():
                if c["name"] == marker:
                    self.inner_map = c["inner_map"]
                    print("Inner map found")
        else:
            print("There are no inner maps")

    def RetrievePdfInnerMap(self, input_name):
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Academy"]

        for c in col.find():
            if c["name"] == input_name:
                self.inner_map = c["inner_map"]

    def DownloadPdf(self):
        # download to phone
        pass
