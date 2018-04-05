from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

data_alda = "Introduction to the problems and techniques for automated discovery of knowledge in databases. Topics include representation, evaluation, and formalization of knowledge for discovery; classification, prediction, clustering, and association methods.Selected applications in commerce, security, and bioinformatics. Students cannot get credit for both CSC 422 and CSC 522."

words_no_punct = tokenizer.tokenize(data_alda)
data = ' '.join(words_no_punct)

stop_words = set(stopwords.words('english'))
words = [w for w in word_tokenize(data) if w not in stop_words]

print(words)
