mylist=['stuff','words','testing','python','train','plane','hype','stuff','antidisestablishmentarianism','testing','more','list','long','train','train','point']
long = '' #Creating a blank variable so any word will contain more "letters" than long.
for i in mylist:
        if len(i)>len(long):
            long=i
print("From the list:")
print(mylist,"\n")

print("The longest word of your list is:",long)