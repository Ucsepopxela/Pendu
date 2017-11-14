import os
CurrDir = os.getcwd()
os.chdir(CurrDir)

mylist=[]

F=open("words.txt","r")
for line in F:
    line=line.lower()
    counter=line.count(line)
    print(line,counter)
    mylist.append(line)

mylist.sort()

print(mylist)