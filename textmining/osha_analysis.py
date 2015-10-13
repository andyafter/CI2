from data import *
from bad_data import *


osha_data = osdata[1:]
osha_cause = {}

# how many types of death causes 
for i in osha_data:
	if i[1] not in osha_cause:
		osha_cause[i[1]] = 1
	else:
		osha_cause[i[1]] += 1

# filter the death cause words
death_words = {}
for i in osha_cause:
	temp = ''
	for symbol in symbols:
		for word in i.split():
			temp = word.replace(symbol, ' ')
	if temp in death_words:
		death_words[temp] += 1
	else:
		death_words[temp] = 1

print death_words

