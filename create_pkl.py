import pickle

f = open('.cred.pkl', 'wb')
user = "rtrgntsg"
password = "Rouknechovvosh4"
pickle.dump((user, password), f, protocol=pickle.HIGHEST_PROTOCOL)
f.close()