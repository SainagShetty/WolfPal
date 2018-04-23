from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import nltk
import pprint as pp
import db_scripts
import pprint
import pickle
import json
import sys

def get_credentials():
    pkl_file = open('.cred.pkl', 'rb')
    data = pickle.load(pkl_file)
    return data[0], data[1], data[2], data[3]

def load_stop_words(stop_word_file):
    stop_words = []
    fo = open(stop_word_file)
    for line in fo:
        if line.strip()[0:1] != "#":
            for word in line.split():  # in case more than one per line
                stop_words.append(word)
    fo.close()
    return stop_words

def load_keywords_from_bucket(keyword_file):
    word_map = dict()
    file = open(keyword_file)
    for line in file:
        key = line.split(':')
        #print(key)
        x, y = Keywords(key[1]).fetch()
        y = list(set(y))
        if key[0] in word_map:
            val = word_map[key[0]]
            val = [j for i in zip(val,y) for j in i]
            word_map[key[0]] = val
        else:
#             val = list()
#             val.append(y)
            word_map[key[0]] = y
    file.close()
    return word_map

def load_keywords_from_json(json_file):
    fp = open(json_file, 'r')
    word_map = json.load(fp)
    #print(word_map['Algorithm'])
    fp.close()
    return word_map

def remove_puncts(text):
    tokenizer = RegexpTokenizer(r'\w+')
    words_no_punct = tokenizer.tokenize(text)
    data = ' '.join(words_no_punct)
    return data

def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False

def generate_candidate_keywords(data, stop_words):
    words = [w for w in word_tokenize(
        data) if w.lower() not in stop_words and not is_number(w)]
    return words

def stem_lemmatize(keywords):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    tokenizer = RegexpTokenizer(r'\w+')
    x = []
    y = []
    for word in keywords:
        x.append(stemmer.stem(word))
        y.append(lemmatizer.lemmatize(word))
    return x

def get_percentage_mapping(topic, lemma):
    mapping = [value for value in topic if value in lemma]
    #mapping = [list(filter(lambda x: x in topic, sublist)) for sublist in lemma]
    #print(mapping)
    return (len(mapping)/len(topic))


class Keywords:
    def __init__(self, text):
        self.text = text
        self.stop_words = load_stop_words("FoxStopList.txt")

    def fetch(self):
        candidate = remove_puncts(self.text)
        keywords = generate_candidate_keywords(candidate, self.stop_words)
        # table = stem_lemmatize(keywords)
        st = stem_lemmatize(keywords)
        return keywords, st
    def map_keywords(self):
        topic_map = load_keywords_from_bucket("keywords.txt")
        stem, lemma = self.fetch()
        percent_mapping = {}
        topic = ''
        maxi = 0
        for key in topic_map.keys():
            percent = get_percentage_mapping(topic_map[key],lemma)
            percent_mapping[key] = percent 
        percent = sorted(percent_mapping.items(), key=lambda x:x[1])
        t = [x[0] for x in percent[::-1][:2]]
        return t

def load_course_map(json_file):
    fp = open(json_file, 'r')
    course_map = json.load(fp)
    fp.close()
    return course_map

def get_course_lists(userinput):
	course_map = load_course_map('course-map.json')
	# print(course_map['Algorithms'])

	userinput = str(userinput)
	words = Keywords(userinput).map_keywords()
	course_list = []
	for i in words:
		try:
			course_list.extend(course_map[i])
		except:
			pass
		
	course_list = set(course_list)
	# print(words)
	return course_list


print(get_course_lists(sys.argv))
# username, password, db_name, collection_name = get_credentials()
# print(course_list)
# print("Number of courses: ",len(course_list))
# for course_id in course_list:
# 	row = db_scripts.db_retrieve(username, password, db_name, collection_name, course_id)
# 	print(row['course_name'])


