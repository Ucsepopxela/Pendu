mylist=['stuff','words','testing','python','train','plane','hype','stuff','antidisestablishmentarianism','testing','more','list','long','train','train','point']

print("Here is the list of words we have:")
print(mylist)

removal=input("What word would you like to remove?\n")
removal = removal.lower()  #To make sure if they are capital letters it'll still work.

if removal in mylist:
    for i in range(mylist.count(removal)):
        mylist.remove(removal)
    print("Here is the ne list:",mylist)
else:
    print(removal,"is not part of the list.")
