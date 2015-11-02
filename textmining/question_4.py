# -*- coding: utf-8 -*-
import pandas as pd
from nltk.corpus import stopwords
import string
from nltk import word_tokenize
from nltk import pos_tag
from nltk import sent_tokenize
from nltk import Tree
from nltk import RegexpParser
import re
import csv
from collections import Counter

import os
os.chdir(os.path.dirname(__file__))

def chunkingList(dataS, chunkgram):
    """
    This function will find the chunk
    """
    #data = str(dataS)
    words = word_tokenize(str(dataS)[1:])
    #print words
    ps = pos_tag(words)

#    print ps
    
    chunkParser = RegexpParser(chunkgram)
    chunked = chunkParser.parse(ps)
    #print chunked
    tree = Tree('s', chunked)
    docs = []
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'Chunk'):
        # Assemble the chunk into one line and strip extra punctuations
        docs.append(" ".join([a for (a,b) in subtree.leaves()]))
    return docs
    
def writeFile(name, givenList):
    """
    Write lists to csv for further analysis and sharing
    """
    with open(name, 'wb') as f:
        writer = csv.writer(f)
        for val in givenList:
            writer.writerow([val])
#
data = pd.read_csv("classification/MsiaAccidentCases.csv")

caseTitle = data["Summary Case"]

data = pd.read_csv("classification/osha.csv")

caseTitle = data["summary"]

# Remove the empty rows
caseTitle = caseTitle.dropna()
caseTitle1 = caseTitle.tolist()
# get the first sentence of summary case
objects = [sent_tokenize(line)[0] for line in caseTitle1]

# Grammar for chunking the activity, and represented in
# past continuous tense, and ends with noun phrase.
grammar = r"""Chunk:{<VB.?>+<VBG|VBR|JJ><RB.?>*<IN>*<DT>*<JJ.?>*<NN.?>*<DT>*<NN.?>}"""

chunks = chunkingList(objects, grammar)

# Remove stopwords 
pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
text = [pattern.sub('', line) for line in chunks]
text = [line.translate(None, string.punctuation) for line in text]

# Getting the string where action was performed
regexp = re.compile(r'ing')
activitiesFinal = [j for j in text if regexp.search(j) is not None]


grammar = r"""Chunk:{<VBG|JJ>+}"""

chunks2 = chunkingList(activitiesFinal, grammar)

top100activities = Counter(chunks2).most_common(100)
top100actions =Counter(activitiesFinal).most_common(100)

writeFile('actions.csv', chunks2)
writeFile('activities.csv', activitiesFinal)
