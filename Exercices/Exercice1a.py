mylist=['stuff','words','testing','python','train','plane','hype','stuff','antidisestablishmentarianism','testing','more','list','long','train','train','point']
newlist=[] #Creating the new list for the new words without first and last characters

#Removal process
for i in mylist:
    x=i[1:-1] #The word is saved in variable x without value 0 which is the first letter and -1 which is the letter before the end.
    newlist.append(x)

print("Here is your original list:")
print(mylist,"\n")

print("Here is the new list without the first and last characters of the list:")
print(newlist)