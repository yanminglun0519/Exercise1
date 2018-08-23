F = open('words.txt','r' )
allWords = F.read()
listAll = allWords.split(" ")
f = open('Q1.txt','w')
words = {}

for word in listAll:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

for key, values in words.items():
    print(key,values)
    f.write(key+' '+str(values)+'\n')