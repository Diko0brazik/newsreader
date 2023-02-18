import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

mystem = Mystem() 
russian_stopwords = stopwords.words("russian")


def countwords(sentence, lang='russian'):
    #mystem = Mystem() 
    #russian_stopwords = stopwords.words("russian")

    tokens = mystem.lemmatize(sentence.lower())
    tokens = [token for token in tokens if token not in russian_stopwords\
              and token != " " \
              and token.strip() not in punctuation]

    #words = nltk.word_tokenize(sentence)
    fdist1 = nltk.FreqDist(tokens)
    return(fdist1.most_common())

if __name__ == "__main__":
    s = 'красивая Зи лежала лежал'
    print(countwords(s))