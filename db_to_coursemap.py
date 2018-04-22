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
        topic_map = load_keywords_from_json("keywords.json")
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

# def load_keywords_from_bucket(keyword_file):
#     word_map = dict()
#     file = open(keyword_file)
#     for line in file:
#         key = line.split(':')
#         #print(key)
#         x, y = Keywords(key[1]).fetch()
#         y = list(set(y))
#         if key[0] in word_map:
#             val = word_map[key[0]]
#             val = [j for i in zip(val,y) for j in i]
#             word_map[key[0]] = val
#         else:
#             word_map[key[0]] = y
#     file.close()
#     return word_map

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

# course_map = {}

def modify_course_map(domain, course_id):
    for topic in domain:
        if topic in course_map.keys(): 
            course_map[topic].append(course_id)
        else:
            course_map[topic] = [course_id]
    
# modify_course_map(['Data Science', 'Algorithms'],  'CSC522')
# course_map

def database_retrieve():
    username, password, db_name, collection_name = get_credentials()
    all_courses = db_scripts.db_fetch_all(username, password, db_name, collection_name)
    for course in all_courses:
        percent = Keywords(course['description']).map_keywords()
        modify_course_map(percent, course['course_id'])
# database_retrieve()
def coursemap_to_json(course_map):
	file = open('course-map.json', 'w+')
	json.dump(course_map, file, sort_keys=True, indent=4)
	file.close()

if __name__ == "__main__":
	course_map = {}
	database_retrieve()
	coursemap_to_json(coursemap_to_json)

