from data import *
from bad_data import *


mlac_data = mldata[1:]
mlac_cause = {}

# how many types of death causes 
for i in mlac_data:
	if i[1] not in mlac_cause:
		mlac_cause[i[1]] = 1
	else:
		mlac_cause[i[1]] += 1

# filter the death cause words
death_words = {}
for i in mlac_cause:
	temp = ''
	for symbol in symbols:
		for word in i.split():
			temp = word.replace(symbol, ' ')
	if temp in death_words:
		death_words[temp] += 1
	else:
		death_words[temp] = 1

print death_words

