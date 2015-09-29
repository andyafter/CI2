import logging, gensim, bz2

id2word = gensim.corpora.Dictionary.load_from_text('/Users/andypan/Desktop/wikidata/wiki_prepared_wordids.txt')
mm = gensim.corpora.MmCorpus('/Users/andypan/Desktop/wikidata/wiki_prepared_tfidf.mm')
lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=1, chunksize=10000, passes=1)
