from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from beautifultable import BeautifulTable
import re
import nltk
import pprint as pp
import db_scripts


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
    words = [w for w in word_tokenize(
        data) if w.lower() not in stop_words and not is_number(w)]
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
        table.append_row(
            [word, lemmatizer.lemmatize(word), stemmer.stem(word)])
        x.append(stemmer.stem(word))
        y.append(lemmatizer.lemmatize(word))
    return table


alda = "Introduction to the problems and techniques for automated discovery of knowledge in databases. Topics include representation, evaluation, and formalization of knowledge for discovery; classification, prediction, clustering, and association methods.Selected applications in commerce, security, and bioinformatics. Students cannot get credit for both CSC 422 and CSC 522."
# doc1 = "Fundamental issues related to the design of operating systems. Process scheduling and coordination, deadlock, memory management and elements of distributed systems."
# doc2 = "Algorithm design techniques: use of data structures, divide and conquer, dynamic programming, greedy techniques, local and global search. Complexity and analysis of algorithms: asymptotic analysis, worst case and average case, recurrences, lower bounds, NP-completeness. Algorithms for classical problems including sorting, searching and graph problems [connectivity, shortest paths, minimum spanning trees]."
# doc3 = "Introduces students to the discipline of designing, developing, and testing secure and dependable software-based systems. Students will learn about risks and vulnerabilities, and effective software security techniques. Topics include common vulnerabilities, access control, information leakage, logging, usability, risk analysis, testing, design principles, security policies, and privacy. Project required."
# doc4 = "Introduction to and overview of artificial intelligence. Study of AI programming language such as LISP or PROLOG. Elements of AI problem-solving technique. State spaces and search techniques. Logic, theorem proving and associative databases. Introduction to knowledge representation, expert systems and selected topics including natural language processing, vision and robotics."
# doc5 = "Basic theory and concepts of human-computer interaction. Human and computational aspects. Cognitive engineering. Practical HCI skills. Significant historical case studies. Current technology and future directions in user interface development."
# doc6 = "The conception and creation of effective visual interfaces for mobile devices, including ideation and prototyping for useful mobile applications, the industry and architecture of mobile devices, mobile usage context, computer graphics and interfaces for mobiles, and mobile programming."
# doc7 = "Topics related to design and management of campus enterprise networks, including VLAN design; virtualization and automation methodologies for management; laboratory use of open space source and commercial tools for managing such networks."
# doc8 = "Algorithm behavior and applicability. Effect of roundoff errors, systems of linear equations and direct methods, least squares via Givens and Householder transformations, stationary and Krylov iterative methods, the conjugate gradient and GMRES methods, convergence of method."

# user = "I like Artificial Intelligence"
# course = {
#     "CSC522": ["Introduction to the problems and techniques for automated discovery of knowledge in databases. Topics include representation, evaluation, and formalization of knowledge for discovery; classification, prediction, clustering, and association methods.Selected applications in commerce, security, and bioinformatics. Students cannot get credit for both CSC 422 and CSC 522."],
#     "CSC501": ["Fundamental issues related to the design of operating systems. Process scheduling and coordination, deadlock, memory management and elements of distributed systems."],
#     "CSC505": ["Algorithm design techniques: use of data structures, divide and conquer, dynamic programming, greedy techniques, local and global search. Complexity and analysis of algorithms: asymptotic analysis, worst case and average case, recurrences, lower bounds, NP-completeness. Algorithms for classical problems including sorting, searching and graph problems [connectivity, shortest paths, minimum spanning trees]."],
#     "CSC510": ["Introduction to and overview of artificial intelligence. Study of AI programming language such as LISP or PROLOG. Elements of AI problem-solving technique. State spaces and search techniques. Logic, theorem proving and associative databases. Introduction to knowledge representation, expert systems and selected topics including natural language processing, vision and robotics."],
# }
# stop_words = load_stop_words("FoxStopList.txt")
# candidate = remove_puncts(user)
# keywords = generate_candidate_keywords(candidate, stop_words)
# # pp.pprint(keywords)
# table = stem_lemmatize(keywords)
# print(table)


class Keywords:
    def __init__(self, text):
        self.text = text
        self.stop_words = load_stop_words("FoxStopList.txt")

    def fetch(self):
        candidate = remove_puncts(self.text)
        keywords = generate_candidate_keywords(candidate, self.stop_words)
        # table = stem_lemmatize(keywords)
        table = stem_lemmatize(keywords)
        return keywords

# l = Keywords(alda).fetch()
# print(l)

# rec = db_scripts.db_retrieve("wolfpal","courses", "CSC", "501")
# tmp= Keywords(rec['desc']).fetch()
# db_scripts.db_update("wolfpal","courses", "CSC", "501", "keywords",tmp)


all_courses = db_scripts.db_fetch_all("wolfpal", "courses")
for course in all_courses:
    tmp = Keywords(course['desc']).fetch()
    db_scripts.db_update("wolfpal", "courses",
                         course["branch"], course["number"], "keywords", tmp)
