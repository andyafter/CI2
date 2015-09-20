import numpy as np
import xml.etree.ElementTree as xml
import logging, gensim, bz2

from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel
from itertools import izip

# this script is for the test of some of the text mining stuff and LDA in python

# I'm not sure how long will it take to load this file, the file is about 7 GB size
#articles = xml.parse('/Users/andypan/Desktop/wikidata/enwikisource-20150901-pages-articles.xml').getroot()

# you should follow this link: https://radimrehurek.com/gensim/wiki.html

doc = ["Carly Fiorina likes to joke that she used to be 'really unemployable' =",
       "The Republican presidential hopeful graduated from Stanford University with a degree in medieval history and philosophy",
       "after which she went to law school",
       "She hated it so much, she quit after a single semester",
       "Eventually, Fiorina got a job as a receptionist: typing, filing and answering the phone"]

stoplist = set('for a of the and to in she he after which it quite ='.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in doc]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]
         for text in texts]


dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# initialize a document
tfidf = models.TfidfModel(corpus)

# I can print out the topics for LSA
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus]

for l,t in izip(corpus_lsi,corpus):
    print l,"#",t
print
for top in lsi.print_topics(2):
    print top

# I can print out the documents and which is the most probable topics for each doc.
lda = ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=50)
corpus_lda = lda[corpus]

for l,t in izip(corpus_lda,corpus):
    print l,"#",t
print

# But I am unable to print out the topics, how should i do it?
for top in lda.print_topics(10):
    print top
