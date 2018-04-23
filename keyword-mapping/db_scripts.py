from pymongo import MongoClient
import json
import pickle

def db_connect(username, password, db_name):
    # get connection object to the server space
    client = MongoClient("ds239359.mlab.com", 39359, connectTimeoutMS=30000,
                         socketTimeoutMS=None, socketKeepAlive=True)
    # select the database name which you want to work on
    db = client[db_name]
    # authenticate connection to the database. Without this your object won't be able to read/write from/to the database
    try:
        db.authenticate(username, password)
        # print("Authentication Successful.")
        # return the authenticated database handle
        return db
    except:
        # print("Authentication failed. You must try again.")
        pass

def db_insert(username, password, db_name, collection_name, course_id, course_name, semester, description, day="NA", time="NA", project="NA", fieldwork="NA", ratings=-1):
        
    db = db_connect(username, password, db_name)
    json_details = json.dumps(
        {
            'course_id': course_id,
            'course_name': course_name,
            'semester': semester,
            'day': day,
            'time': time,
            'project': project,
            'fieldwork': fieldwork,
            'ratings': ratings,
            'description': description
        }, default=string_converter)
    entry = json.loads(json_details)
    try:
        db[collection_name].insert_one(entry)
        print("Insertion Successful")
    except:
        print("Sorry we encountered some error in inserting.")

def string_converter(o):
    if isinstance(o, datetime):
        return o.__str__() 

def db_update(username, password, db_name, collection_name, branch, number, record_key, record_val):
    db = db_connect(username, password, db_name)
    try:
        db[collection_name].update_one({
            'branch': branch,
            'number': number
        },
            {
            '$set': {
                record_key: record_val
            }
        })
        print("Update Successful")
    except:
        print("Sorry we encountered some error in updating.")


def db_fetch_all(username, password, db_name, collection_name):
    db = db_connect(username, password,db_name)
    pymongo_cursor = db[collection_name].find()
    all_data = list(pymongo_cursor)
    return all_data


def db_retrieve(username, password, db_name, collection_name, course_id):
    db = db_connect(username, password,db_name)
    query = json.dumps({
        'course_id': course_id
    })
    query = json.loads(query)
    try:
        data = db[collection_name].find_one(query)
        # print("Successfully Retrieved")
        return data
    except:
        # print("Sorry we encountered some error in retrieving.")
        pass

# pkl_file = open('.cred.pkl', 'rb')
# data = pickle.load(pkl_file)
# print(data['user'])
# print(data['password'])
