mylist=['stuff','words','testing','python','train','plane','hype','stuff','antidisestablishmentarianism','testing','more','list','long','train','train','point']

newlist=' '.join(mylist) #We make the list into a string so we can replace the words easily.

k=input("Insert the word you want to replace:")
k=k.lower()
l=input("Insert the new word:")
l=l.lower()
print("\n")

print("Here is you new list with '",k,"' replaced by '",l,"'.")
print(newlist.replace(k,l)) #We replace the word 'k' by the word 'l' in the string "newlist".