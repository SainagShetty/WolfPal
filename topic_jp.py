
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
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


doc_complete


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

doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=3, num_words=3))
#[0.168*health + 0.083*sugar + 0.072*bad,0.061*consume + 0.050*drive + 0.050*sister,0.049*pressur + 0.049*father + 0.049*sister]

