# -*- coding: utf-8 -*-


# Import all packages

import pandas as pd
from nltk.corpus import stopwords
import string
from nltk import word_tokenize
import nltk
from nltk import pos_tag
import csv

data = pd.read_csv("classification/osha.csv")

caseTitle = data["object cause accident"]

stopwordsList = stopwords.words('english')

contextualStopwords = [u'fall',u'burns',u'contact',u'equipment',u'face', 
u'falling', u'']
stopwordsList.extend(contextualStopwords)

caseTitle = [x for x in caseTitle if str(x) != 'nan']
labelled = []
for row in caseTitle:
    text_nopunc = row.translate(string.maketrans("", ""), string.punctuation)
    # text_nopunc=text_nopunc.lower()
    labelled.append(text_nopunc)
    # labelled = labelled.append(word_tokenize(labelled))

p = []
for row in caseTitle:
    row = row.lower()
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
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
        yield subtree.leaves()


def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    # word = stemmer.stem_word(word)
    # word = lemmatizer.lemmatize(word)
    return word


def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwordsList)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [normalise(w) for w, t in leaf if acceptable_word(w)]
        yield term
            
            
chunker = nltk.RegexpParser(grammar)


n = 0
death_causes = {}
death_words = {}
all_objects = ['common objects']
sort_terms = {}

for r in p:
    # print nltk.ne_chunk(r)
    # print chunker.parse(r)
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
            all_objects.append(word)     
#            print word,
#        print ","
        if t not in death_causes:
            death_causes[t] = 1
        else:
            death_causes[t] += 1

death_causes[''] = None
sort_terms = sorted(death_causes.iteritems(), key=lambda asd: asd[1], reverse = True)

for i in range(0, 10, +1):
    print sort_terms[i]
    

with open('common_objects.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in all_objects:
        writer.writerow([val])

