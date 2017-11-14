mylist=['stuff','words','testing','python','train','plane','hype','stuff','antidisestablishmentarianism','testing','more','list','long','train','train','point']
newlist=[] #Creating the new list for the length of the words.

#Length check process and adding the length to the newlist.
for i in mylist:
    x=len(i) #The word's length is saved in variable x to be added to the new list.
    newlist.append(x)

print("Here is your list:")
print(mylist,"\n")

print("Here is the new list with the number of characters of each word in the right order:")
print(newlist)