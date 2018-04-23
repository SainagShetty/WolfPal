from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
import numpy as np

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
doc9 = "The need for parallel and massively parallel computers. Taxonomy of parallel computer architecture, and programming models for parallel architectures. Example parallel algorithms. Shared-memory vs. distributed-memory architectures. Correctness and performance issues. Cache coherence and memory consistency. Bus-based and scalable directory-based multiprocessors. Interconnection-network topologies and switch design. Brief overview of advanced topics such as multiprocessor prefetching and speculative parallel execution. Credit is not allowed for more than one course in this set: ECE 406, ECE 506, CSC 406."
doc10 = "The design of object-oriented systems, using principles such as the GRASP principles, and methodologies such as CRC cards and the Unified Modeling Language [ULM]. Requirements analysis. Design patterns Agile Methods. Static vs. dynamic typing. Metaprogramming. Open-source development practices and tools. Test-first development. Project required, involving contributions to an open-source software project"
doc11= "Modern software development organizations require entire teams of DevOps to automate and maintain software engineering processes and infrastructure vital to the organization. In this course, you will gain practical exposure to the skills, tools, and knowledge needed in automating software engineering processes and infrastructure. Students will have the chance to build new or extend existing software engineering tools and design a DevOps pipeline."
doc12 = "Introduction to and overview of artificial intelligence. Study of AI programming language such as LISP or PROLOG. Elements of AI problem-solving technique. State spaces and search techniques. Logic, theorem proving and associative databases. Introduction to knowledge representation, expert systems and selected topics including natural language processing, vision and robotics."
doc13 = "Study of cloud computing principles, architectures, and actual implementations. Students will learn how to critically evaluate cloud solutions, how to construct and secure a private cloud computing environment based on open source solutions, and how to federate it with external clouds. Performance, security, cost, usability, and utility of cloud computing solutions will be studied both theoretically and in hands-on exercises. Hardware-, infrastructure-, platform-, software-, security-, and high-performance computing - as-a-service."
doc14 = "This course surveys the field of social computing, introducing its key concepts, paradigms, and techniques. Specific topics are selected from the following list: social media and social network analytics, sociological underpinnings, crowdsourcing and surveys, human computation, social mobilization, human decision making, voting theory, judgment aggregation, prediction markets, economic mechanisms, incentives, organizational modeling, argumentation, contracts, norms, mobility and social context, sociotechnical systems, and software engineering with and for social computing. This course incorporates ideas from diverse disciplines [including sociology, psychology, law, economics, political science, logic, statistics, philosophy, business] to provide essential background for future computer science careers in industry and research."
doc15 = "This course offers an advanced discussion of topics in computer graphics, with an emphasis on rendering techniques and GPU shader programming used in computer game engine design. Students are required to implement a medium-size game program that includes modeling and rendering, 2D physics, and animation of dynamic objects. Students will learn about GPU basics, mathematics of transformations, visual appearance properties, texturing, global illumination, and toon shading in computer games."
doc16 = "A theoretical and practical study of the computational models supporting the creation of interactive narrative systems. Topics include basic introductions to cognitive, linguistic and film theoretic models of narrative; representations and reasoning techniques from artificial intelligence related to the creation of storylines, dialog, camera control and other features of narrative in text-based and/or 3D virtual worlds; mechanisms for controlling character behavior in multi-agent multi-user stories; and applications of these techniques ranging from interactive entertainment to educational software to training simulations."
doc17 = "In this course we will examine Artificial Intelligence [AI] techniques that are used in the design of computer games. We will look at techniques for game playing as well as the design of AI opponents tasked with creating good experiences for players. The course will begin with a discussion of general AI, common algorithms, data structures, and representations. From there, we will cover topics in character movement, pathfinding, decision making, strategy, tactics, and learning. In a sequence of programming assignments students will create increasingly sophisticated AI implementations. Students will also critically review the projects conducted by graduate students enrolled in CSC584. CSC majors only. Students cannot get credit for both CSC 484 and CSC 584."
doc18 = "This course addresses the human aspect of software engineering, by studying the people who practice it. Students will explore software engineering as traditionally defined, and also consider techniques that transform how we understand software engineering, such as methods from psychology and sociology. Students will study the usability of software engineering tools, the psychology of programming, performance of software developers, experimental methods in observing software engineers, distributed development and coordination, and cultural differences between software developers."
doc19 = "An advanced introduction to software testing and reliability. The course is a balanced mixture of theory, practice, and application. Methods, techniques, and tools for testing software and producing reliable and secure software are used and analyzed. Software reliability growth models and techniques for improving and predicting software reliability are examined, and their practical use is demonstrated. Good knowledge of C++ or Java. Knowledge of the basics of statistics, calculus, and linear algebra."
doc20 = "Concepts, theories, and techniques for computing with services. This course examines architectures for Web applications based on the classical publish, find, and bind triangle, but formulates it at a higher level. It considers sophisticated approaches for the description, discovery, and engagement of services, especially over the Web and the Grid. This course emphasizes service composition. Key topics include semantics, transactions, processes, agents, quality of service, compliance, and trust."
# compile documents
documents = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9, doc10, doc11, doc12, doc13, doc14, doc15, doc16, doc17, doc18, doc19, doc20]
#test_doc = [doc7, doc8]

no_features = 10

# NMF is able to use tf-idf
tfidf_vectorizer = TfidfVectorizer(max_df=1.0, min_df=0.0, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(documents)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=1, min_df=0.01, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()

no_topics = 5

# Run NMF
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

# Run LDA
lda = LatentDirichletAllocation(n_components=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

# X_test = tf_vectorizer.transform(test_doc)
# doc_topic_dist_unnormalized = np.matrix(lda.transform(X_test))

# # normalize the distribution (only needed if you want to work with the probabilities)
# doc_topic_dist = doc_topic_dist_unnormalized/doc_topic_dist_unnormalized.sum(axis=1)

# print doc_topic_dist.argmax(axis=1)


no_top_words = 10
print "NMF Topics"
display_topics(nmf, tfidf_feature_names, no_top_words)
print "LDA Topics"
display_topics(lda, tf_feature_names, no_top_words)