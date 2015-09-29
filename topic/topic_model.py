import numpy as np
import xml.etree.ElementTree as xml
import logging, gensim, bz2

from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel
from itertools import izip

