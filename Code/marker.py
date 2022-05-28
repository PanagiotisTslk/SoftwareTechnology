# Connection with database
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://tslk:Tslkgtx950pt@cluster0.jnvsh.mongodb.net/StudentUp"
    CONNECTION_STRING = "mongodb+srv://tslk:Tslkgtx950pt@cluster0.jnvsh.mongodb.net/StudentUp"
    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]

# myclient = pymongo.MongoClient("mongodb+srv://tslk:Tslkgtx950pt@cluster0.jnvsh.mongodb.net/StudentUp")
# mydb = myclient["StudentUp"]
# mycol = mydb["Marker"]

# get_database()


# Connecting with database
dbname1 = get_database()
# Choosing collection
col1 = dbname1["Marker"]
# print(col1)

marker = {
            "name": ['ceid', 'estia'],
            "coordinates": [[2000012120, 2000902120], [2012001212, 20120011315]],
            "kind": ["academy", "uni_location"],
            "color": ["red", "red"],
            "data": ["ceid_info.txt", "estia_info.txt"],
            "timetable": ["09:00-21:00", "07:00-16:00"]
        }

# x = mycol.insert_one(marker)

col1.insert_one(marker)
for x in col1.find():
    print(x)

# print("Markers created successfully!")
# for x in mycol.find():
#     print(x)


# Class for Markers
class Marker:

    # Constructor
    def __init__(self, name, coordinates, kind, color, data, timetable):
        self.name = name
        self.coordinates = coordinates
        self.kind = kind
        self.color = color
        self.data = data
        self.timetable = timetable

    def RetrieveCoord(self):
        # many objects ?
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers"]

        list_with_markers = []

        for c in col.find():
            self.coordinates = c['coordinates']
            list_with_markers.append(self.coordinates)

    def CheckOpenMarks(self):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers_Map_list"]

        for c in col.find():
            if current_time > self.timetable or current_time > self.timetable:
                self.RemoveClosedMarks()

    def RemoveClosedMarks(self):
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers_Map_List"]

        # $pull: {'coordinates': str(self.coordinates)}
        # print()  # remove marker from list

    def RetrieveMarkerInfo(self, marker_touch):
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers"]

        for c in col.find():
            if c['name'] == marker_touch:
                self.data = c['data']

        return self.data
        # print(self.data)

    def CheckLoc(self, name):
        # Connecting with database
        dbname = get_database()
        # Choosing collection
        col = dbname["Markers"]

        for c in col.find():
            if c['name'] == name:
                self.coordinates = c['coordinates']
                return True
        else:
            return False

    def LocAnalysis(self, name: str):
        new_name = name.upper()
        self.RetrieveMarker(new_name)

    def RetrieveMarker(self, name):
        isloc = self.CheckLoc(name)
        if isloc:
            return self.coordinates
        else:
            print("Location don't found")
