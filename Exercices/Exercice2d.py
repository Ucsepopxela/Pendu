import os
CurrDir = os.getcwd()
os.chdir(CurrDir)


newlist=' '.join(mylist) #We make the list into a string so we can replace the words easily.

k=input("Insert the word you want to replace:")
k=k.lower()
print("\n")

print("Here is you new list with '",k,"' replaced by '",l,"'.")
print(newlist.replace(k,l)) #We replace the word 'k' by the word 'l' in the string "newlist".