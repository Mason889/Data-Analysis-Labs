from stop_words import get_stop_words
from string import punctuation

stopWordsRu = get_stop_words('ru')

stop_words_upper = [i.upper() for i in stopWordsRu]     # convert stop_words in uppercase
for spec in punctuation:                                # add in stop_words list spec symbols
    stop_words_upper.append(spec)

all_words = open('words.json', 'r')
data = eval(all_words.read())                   # get data from words.json file
all_words.close()

for element in stop_words_upper:                # removing of all stopwords in source words dict
    if element in data:
        data.pop(element) 

iterator = 0

for k in sorted(data, key=data.get, reverse=True):
    if iterator <= 20:
        iterator += 1
        print(k, data[k])
    else:
        break