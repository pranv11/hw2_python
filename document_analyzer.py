file1 = open('homework2/document.txt', encoding='utf8')

sentence = file1.read()

noPeriod_Sen = sentence.replace(".","")

sentence_list = noPeriod_Sen.split()

unique = []
for word in sentence_list:
    if word not in unique:
        unique.append(word)

unique.sort()

value = []
for i in range(len(unique)):
    value.append(sentence_list.count(unique[i]))

dictionary_sen = {}

for i in range(len(unique)):
    dictionary_sen [unique[i]] = value[i]


dictionary_sorted = sorted(dictionary_sen , key=dictionary_sen.get, reverse=True)[:5]


for i in range(len(dictionary_sorted)):
    print('/r'+ str(dictionary_sorted[i]) + ": " + str(dictionary_sen[dictionary_sorted[i]]))


