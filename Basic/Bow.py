#importing nltk package
import nltk

para = """Yes! The Harry Potter author uses inspiring words to offer lessons
          she learned late and wished others had told her earlier. 
          Rowling was a poor, single mother before her writing shot her 
          into the financial stratosphere, but she doesn’t romanticize poverty. 
         Beyond the humiliation and depression of being poor, she feared failure, 
         and yet it was failure that gave her the lessons she needed to succeed. 
         That might be unexpected, but it’s also motivating. 
         Who doesn’t have experience with failure? And we can all succeed."""
#cleaning nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(para)
corpus= []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word)  for word in review  if word not in set(stopwords.words('English'))]
    review = ''.join(review)
    corpus.append(review)
#creating the bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()