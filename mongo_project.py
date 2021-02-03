import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstdb"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a records")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option:")
    return option


def get_record():
    first = input("Enter First name >")
    last = input("Enter  Last name >")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
       print("")
       print("Error! No results found.")

    return doc



def add_record():
    print("")
    first = input("Enter First name >")
    last = input("Enter  Last name >")
    dob = input("Enter Date of Birth >")
    gender = input("Enter Gender >")
    hair_color = input("Enter Hair Color >")
    occupation= input("Enter Occupation >")
    nationality = input("Enter Nationality>")

    new_doc ={
         "first": first.lower(),
         "last": last.lower(),
         "dob": dob,
         "gender": gender,
         "hair_color": hair_color,
         "occupation": occupation,
         "nationality": nationality
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid Option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()