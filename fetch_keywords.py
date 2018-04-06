from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re
import pprint as pp

def load_stop_words(stop_word_file):
    stop_words = []
    for line in open(stop_word_file):
        if line.strip()[0:1] != "#":
            for word in line.split():  # in case more than one per line
                stop_words.append(word)
    return stop_words

def remove_puncts(text):
	tokenizer = RegexpTokenizer(r'\w+')
	words_no_punct = tokenizer.tokenize(text)
	data = ' '.join(words_no_punct)
	return data


def generate_candidate_keywords(data, stop_words):
	words = [w for w in word_tokenize(data) if w not in stop_words]
	return words


data_alda = "Introduction to the problems and techniques for automated discovery of knowledge in databases. Topics include representation, evaluation, and formalization of knowledge for discovery; classification, prediction, clustering, and association methods.Selected applications in commerce, security, and bioinformatics. Students cannot get credit for both CSC 422 and CSC 522."

stop_words = load_stop_words("FoxStopList.txt")
candidate = remove_puncts(data_alda)
pp.pprint(generate_candidate_keywords(candidate, stop_words))


