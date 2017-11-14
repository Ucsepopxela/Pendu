sentence=["I","am","a","boy","i","am","a","girl"]
word="am"
countlist=[]
if word in sentence:
    print( word, " is in the sentence")
    for i, j in enumerate(sentence):
        if j == word:
            countlist.append(i+1)
            #print(word,"is in position",i+1)
print(countlist)