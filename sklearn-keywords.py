from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic %d:" % (topic_idx)
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])

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

no_features = 100

# NMF is able to use tf-idf
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(documents)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()

no_topics = 5

# Run NMF
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

# Run LDA
lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)



no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)
display_topics(lda, tf_feature_names, no_top_words)