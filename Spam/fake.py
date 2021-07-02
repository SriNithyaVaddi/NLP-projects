#anaalyzing the data
#dataset:https://www.kaggle.com/c/fake-news
import pandas as pd
dataset = pd.read_csv('train.csv')
print(dataset.head())
#get the independent feature
x= dataset.drop('label',axis=1)
#get independent features
y =dataset ['label']
print(y.head())
print(dataset.shape)
#create a new dataset to copy the dataset and remove na
dataset = dataset.dropna()
msg = dataset.copy()
msg.reset_index(inplace=True)
msg['text']
print(msg['text'])

#importing the packages of nlp
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
#cleaning the text
ps = PorterStemmer()
wt = WordNetLemmatizer()
corpus=[]
for i in range(0,len(msg)):
    words = re.sub('[^a-z,A-z]', ' ',msg['text'][i])
    words.lower()
    words.split()
    words = [ps.stem(word) for word in words if word not in set(stopwords.words('English'))]
    words = ' '.join(words)
    corpus.append(words)
# from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer
# tfidf = TfidfVectorizer(max_features=5000,ngram_range=(1,3))
# hf = HashingVectorizer()
# x = tfidf.fit_transform(corpus).toarray()
