from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from beautifultable import BeautifulTable
import re
import nltk
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

def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False

def generate_candidate_keywords(data, stop_words):
	words = [w for w in word_tokenize(data) if w.lower() not in stop_words and not is_number(w)]
	return words

def stem_lemmatize(keywords):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    tokenizer = RegexpTokenizer(r'\w+')
    table = BeautifulTable()
    table.column_headers = ["Actual", "Lemmatize", "Stem"]
    x = []
    y = []
    for word in keywords:
        table.append_row([word, lemmatizer.lemmatize(word), stemmer.stem(word)])
        x.append(stemmer.stem(word))
        y.append(lemmatizer.lemmatize(word))
    print(x)
    print(y)
    return table


alda = "Introduction to the problems and techniques for automated discovery of knowledge in databases. Topics include representation, evaluation, and formalization of knowledge for discovery; classification, prediction, clustering, and association methods.Selected applications in commerce, security, and bioinformatics. Students cannot get credit for both CSC 422 and CSC 522."

stop_words = load_stop_words("FoxStopList.txt")
candidate = remove_puncts(alda)
keywords = generate_candidate_keywords(candidate, stop_words)
# pp.pprint(keywords)
table = stem_lemmatize(keywords)
print(table)

# find_names=nltk.RegexpParser('NAMES:{<NNP><NNP>}')
# breakdown=(pos_tag(word_tokenize(alda)))
# listing = (find_names.parse(breakdown))
# for term in listing.subtrees():
#     print(term)


