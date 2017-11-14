mylist=['stuff','words','testing','python','train','plane','hype','stuff','antidisestablishmentarianism','testing','more','list','long','train','train','point']
countlist=[] #New list to have stock the positions of the word occurence.
k = input("Insert the word to search:")
k=k.lower()

if k in mylist: #If the word inserted is in the list, we will proceed to stock the position of the word.
    print("The word",k,"is in the list.\n")
    for i, j in enumerate(mylist):
        if j == k:
            countlist.append(i+1) #We add the position to the list we created to stock the positions (Python count starts at 0, so we add +1 to have a real position)
    m=mylist.count(k)
    print("The word","'",k,"'","appears",m,"times in positions:",countlist)

else:
    print("The word","'",k,"'","is not in the list, it appears 0 times.")