import pickle

f = open('.cred.pkl', 'wb')
username = "paylot"
password = "wolfpal123"
db_name = "wolfpal"
collection_name = "courses" 
pickle.dump((username, password, db_name, collection_name), f, protocol=pickle.HIGHEST_PROTOCOL)
f.close()