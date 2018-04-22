import pickle

f = open('.cred.pkl', 'wb')
username = "rtrgntsg"
password = "Rouknechovvosh4"
db_name = "WolfPal"
collection_name = "courses" 
pickle.dump((username, password, db_name, collection_name), f, protocol=pickle.HIGHEST_PROTOCOL)
f.close()