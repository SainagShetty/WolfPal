# import sys
#
# a = 5
# b = 11
#
# print("Hii")
# print(a+b)
# print(sys.argv[1])

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import nltk
import pprint as pp
# import db_scripts
import pprint
import pickle
import json
import sys

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


print(get_course_lists(sys.argv[1]))
# username, password, db_name, collection_name = get_credentials()
# print(course_list)
# print("Number of courses: ",len(course_list))
# for course_id in course_list:
# 	row = db_scripts.db_retrieve(username, password, db_name, collection_name, course_id)
# 	print(row['course_name'])


from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
import pprint
# coding: utf-8

# In[11]:


doc1 = "Fundamental issues related to the design of operating systems. Process scheduling and coordination, deadlock, memory management and elements of distributed systems."
doc2 = "Algorithm design techniques: use of data structures, divide and conquer, dynamic programming, greedy techniques, local and global search. Complexity and analysis of algorithms: asymptotic analysis, worst case and average case, recurrences, lower bounds, NP-completeness. Algorithms for classical problems including sorting, searching and graph problems [connectivity, shortest paths, minimum spanning trees]."
doc3 = "Introduces students to the discipline of designing, developing, and testing secure and dependable software-based systems. Students will learn about risks and vulnerabilities, and effective software security techniques. Topics include common vulnerabilities, access control, information leakage, logging, usability, risk analysis, testing, design principles, security policies, and privacy. Project required."
doc4 = "Introduction to and overview of artificial intelligence. Study of AI programming language such as LISP or PROLOG. Elements of AI problem-solving technique. State spaces and search techniques. Logic, theorem proving and associative databases. Introduction to knowledge representation, expert systems and selected topics including natural language processing, vision and robotics."
doc5 = "Basic theory and concepts of human-computer interaction. Human and computational aspects. Cognitive engineering. Practical HCI skills. Significant historical case studies. Current technology and future directions in user interface development."
doc6 = "The conception and creation of effective visual interfaces for mobile devices, including ideation and prototyping for useful mobile applications, the industry and architecture of mobile devices, mobile usage context, computer graphics and interfaces for mobiles, and mobile programming."
doc7 = "Topics related to design and management of campus enterprise networks, including VLAN design; virtualization and automation methodologies for management; laboratory use of open space source and commercial tools for managing such networks."
doc8 = "Algorithm behavior and applicability. Effect of roundoff errors, systems of linear equations and direct methods, least squares via Givens and Householder transformations, stationary and Krylov iterative methods, the conjugate gradient and GMRES methods, convergence of method."
# compile documents
doc_complete = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]

# In[12]:


document = ['automated', 'discovery', 'knowledge', 'database', 'representation', 'evaluation', 'formalization', 'knowledge', 'discovery', 'classification', 'prediction', 'clustering', 'association', 'method', 'application', 'commerce', 'security', 'bioinformatics']

# In[13]:


stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()


# In[14]:


def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


# In[15]:


doc_clean = [clean(doc).split() for doc in doc_complete]


# In[16]:


dictionary = corpora.Dictionary(doc_clean)
for x in dictionary:
    print (x)
    for y in dictionary[x]:
        print (y,':',dictionary[x][y])
#dictionary = corpora.Dictionary.load_from_text(doc_complete)
#dictionary = corpora.Dictionary(document)

doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=8, id2word = dictionary, passes=50)

pprint.pprint(ldamodel.print_topics(num_topics=8, num_words=4))
#[0.168*health + 0.083*sugar + 0.072*bad,0.061*consume + 0.050*drive + 0.050*sister,0.049*pressur + 0.049*father + 0.049*sister]


from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer
 
doc1 = "Fundamental issues related to the design of operating systems. Process scheduling and coordination, deadlock, memory management and elements of distributed systems."
doc2 = "Algorithm design techniques: use of data structures, divide and conquer, dynamic programming, greedy techniques, local and global search. Complexity and analysis of algorithms: asymptotic analysis, worst case and average case, recurrences, lower bounds, NP-completeness. Algorithms for classical problems including sorting, searching and graph problems [connectivity, shortest paths, minimum spanning trees]."
doc3 = "Introduces students to the discipline of designing, developing, and testing secure and dependable software-based systems. Students will learn about risks and vulnerabilities, and effective software security techniques. Topics include common vulnerabilities, access control, information leakage, logging, usability, risk analysis, testing, design principles, security policies, and privacy. Project required."
doc4 = "Introduction to and overview of artificial intelligence. Study of AI programming language such as LISP or PROLOG. Elements of AI problem-solving technique. State spaces and search techniques. Logic, theorem proving and associative databases. Introduction to knowledge representation, expert systems and selected topics including natural language processing, vision and robotics."
doc5 = "Basic theory and concepts of human-computer interaction. Human and computational aspects. Cognitive engineering. Practical HCI skills. Significant historical case studies. Current technology and future directions in user interface development."
doc6 = "The conception and creation of effective visual interfaces for mobile devices, including ideation and prototyping for useful mobile applications, the industry and architecture of mobile devices, mobile usage context, computer graphics and interfaces for mobiles, and mobile programming."
doc7 = "Topics related to design and management of campus enterprise networks, including VLAN design; virtualization and automation methodologies for management; laboratory use of open space source and commercial tools for managing such networks."
doc8 = "Algorithm behavior and applicability. Effect of roundoff errors, systems of linear equations and direct methods, least squares via Givens and Householder transformations, stationary and Krylov iterative methods, the conjugate gradient and GMRES methods, convergence of method."
# compile documents
documents = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]
#test_doc = [doc7, doc8]

NUM_TOPICS = 1

vectorizer = CountVectorizer(min_df=1, max_df=6, 
                             stop_words='english', lowercase=True, 
                             token_pattern='[a-zA-Z\-][a-zA-Z\-]{2,}')
data_vectorized = vectorizer.fit_transform(documents)

# Build a Latent Dirichlet Allocation Model
lda_model = LatentDirichletAllocation(n_topics=NUM_TOPICS, max_iter=10, learning_method='online')
lda_Z = lda_model.fit_transform(data_vectorized)
print(lda_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)
 
# Build a Non-Negative Matrix Factorization Model
nmf_model = NMF(n_components=NUM_TOPICS)
nmf_Z = nmf_model.fit_transform(data_vectorized)
print(nmf_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)
 
# Build a Latent Semantic Indexing Model
lsi_model = TruncatedSVD(n_components=NUM_TOPICS)
lsi_Z = lsi_model.fit_transform(data_vectorized)
print(lsi_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)
 
 
# Let's see how the first document in the corpus looks like in different topic spaces
print("LDA")
print(lda_Z[0])
print()
print("NMF")
print(nmf_Z[0])
print()
print("LSI")
print(lsi_Z[0])

def print_topics(model, vectorizer, top_n=10):
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        print([(vectorizer.get_feature_names()[i], topic[i])
                        for i in topic.argsort()[:-top_n - 1:-1]])
 
print("LDA Model:")
print_topics(lda_model, vectorizer)
print("=" * 20)
 
print("NMF Model:")
print_topics(nmf_model, vectorizer)
print("=" * 20)
 
print("LSI Model:")
print_topics(lsi_model, vectorizer)
print("=" * 20)
