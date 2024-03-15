from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from mozg import data_set
from functions import *

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(list(data_set.keys()))

clf = LogisticRegression()
clf.fit(vectors, list(data_set.values()))

del data_set

while True:
    ask = input('Введите ваш промпт:')
    text_vector = vectorizer.transform([ask]).toarray()[0]
    #print(text_vector)
    answer = clf.predict([text_vector])[0]
    func = str(answer).split()[0]
    print(str(answer).replace(func,''))
    exec(func + '()')


