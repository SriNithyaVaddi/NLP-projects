# importing package for nlp
import nltk 
#any paragraph that you liike use
para =  """A warm welcome to you all. 
           I am here to deliver a speech on India. 
           India is one of the ancient civilizations in the world and is also the 7th largest country in the world.
          India is one of the best countries in the world for many reasons, acceptance of people of other religions,
          the closely bonded family culture, the biggest democratic nation, and the fastest-growing economy. 
          With 1.3 billion of population India is the second-largest country in the world. 
         India is God’s favorite country to be blessed with all seasons – spring, summer, monsoon, autumn, pre-winter, and winter. 
         People around the world also recognize India for its Bollywood stardom and Beauty pageants."""
#paragraph into senteces -> tokenzie and then using lemitize or portstemner
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

Ps = PorterStemmer()
wt = WordNetLemmatizer()
sentences = nltk.sent_tokenize(para)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-z,A-Z]',' ', sentences[i] )
    review = review.lower()
    review = review.split()
    review = [ wt.lemmatize(word)for word in  review if word not in set(stopwords.words('English'))]
    #review = [Ps.stem(word)for word in review if word not in set(stopwords.words('English'))]
    #review = [wt.lemitize(word) for word in review if word not in set(stopwords.words('English'))]
    review = ''.join(review)
    corpus.append(review)
#using tf-idf
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
y = tfidf.fit_transform(corpus).toarray()