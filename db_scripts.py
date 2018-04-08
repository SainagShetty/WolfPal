from pymongo import MongoClient
import json

def db_connect(db_name):
	# get connection object to the server space
	client = MongoClient("ds239359.mlab.com", 39359, connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True)
	# select the database name which you want to work on
	db = client[db_name]
	# authenticate connection to the database. Without this your object won't be able to read/write from/to the database
	try:
		db.authenticate("paylot", "wolfpal123")
		print("Authentication Successful.")
		# return the authenticated database handle
		return db
	except:
		print("Authentication failed. You must try again.")

def db_update(db_name, collection_name, branch, number, record_key, record_val):
	db = db_connect(db_name)
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

def db_fetch_all(db_name, collection_name):
	db = db_connect(db_name)
	pymongo_cursor = db[collection_name].find()
	all_data = list(pymongo_cursor)
	return all_data

def db_retrieve(db_name, collection_name, branch, number):
	db = db_connect(db_name)
	query = json.dumps({
		'branch': branch,
		'number': number
	})
	query = json.loads(query)
	try:
		data = db[collection_name].find_one(query)
		print("Successfully Retrieved")
		return data
	except:
		print("Sorry we encountered some error in retrieving.")