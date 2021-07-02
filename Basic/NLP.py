import numpy as np
import  nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
para = """A warm welcome to you all. 
         I am here to deliver a speech on India. 
         India is one of the ancient civilizations in the world and is also the 7th largest country in the world.
         India is one of the best countries in the world for many reasons, acceptance of people of other religions,
         the closely bonded family culture, the biggest democratic nation, and the fastest-growing economy. 
         With 1.3 billion of population India is the second-largest country in the world. 
        India is God’s favorite country to be blessed with all seasons – spring, summer, monsoon, autumn, pre-winter, and winter. 
        People around the world also recognize India for its Bollywood stardom and Beauty pageants."""
sentences = nltk.sent_tokenize(para)
stemmer = PorterStemmer()
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)