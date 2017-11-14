import os
CurrDir = os.getcwd()
os.chdir(CurrDir)

nbrWords=0
nbrChar=0

with open("words.txt") as f:
    for line in f:
        mylist = line.split() #In case there is some sentence
        nbrWords= len(mylist)+nbrWords
        nbrChar= nbrChar+len(line)
print("Word:",nbrWords,"\n""Characters:",nbrChar)