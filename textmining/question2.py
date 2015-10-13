# -*- coding: utf-8 -*-


# Import all packages
import random
import sklearn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn import metrics
from sklearn.feature_selection import SelectKBest, chi2
from sklearn import preprocessing
from pandas import concat
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from nltk.corpus import stopwords

from nltk import pos_tag


data=pd.read_csv("osha.csv")

caseTitle=data["Title Case"]

stopwords = stopwords.words('english')

labelled=[]
for row in caseTitle:
    text_nopunc=row.translate(string.maketrans("",""), string.punctuation)
    #text_nopunc=text_nopunc.lower()
    labelled.append(text_nopunc)
    #labelled = labelled.append(word_tokenize(labelled))
    

p=[]
for row in caseTitle:
    row=row.lower()
    pos = pos_tag(word_tokenize(row))
    p.append(pos)

grammar = r"""
        
        #PP:
            #{<NN|NNP|VB|VBD|VBG|VBN|VBP|VBZ|JJ>*<IN>}
        #PP:
            #{<NN|NNP|VB|VBD|VBG|VBN|VBP|VBZ|JJ|NNS>*<IN|TO>}
        NP: 
            #{<IN|DT|TO><NN.*|VB.*|VBN.*|VBG.*|JJ.*|VBD.*|NNP.*>+}
            {<IN|TO><DT>?<NN.*|NNP.*|NNS.*>+}
            #{<PP><DT|TO>?<NN.*|VB.*|VBN.*|VBG.*|JJ.*|VBD.*|NNP.*>+}
            
"""


def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.node=='NP'):
        yield subtree.leaves()
        
def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    #word = stemmer.stem_word(word)
    #word = lemmatizer.lemmatize(word)
    return word
    
def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted

def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term


chunker = nltk.RegexpParser(grammar)


n = 0
death_causes = {}
death_words = {}

sort_terms = {}

for r in p:
    #print nltk.ne_chunk(r)
    #print chunker.parse(r)
    tree = chunker.parse(r)
    terms = get_terms(tree)
    t = ""
    for term in terms:
        t = " ".join(term)
        for word in term:
            if word not in death_words:
                death_words[word] = 1
            else:
                death_words[word] += 1
            print word,
        print ","
        if t not in death_causes:
            death_causes[t] = 1
        else:
            death_causes[t] += 1
  

sort_terms = sorted(death_causes.iteritems(),key=lambda asd:asd[1],reverse=True)

for i in range(0,10,+1):
    print sort_terms[i]
    
