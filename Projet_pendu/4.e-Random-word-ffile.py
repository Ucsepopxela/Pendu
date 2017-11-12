import os
import random

CurrDir = os.getcwd()
os.chdir(CurrDir)



with open("words.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

print(content)
t = random.randint(0,len(content)-1)
#Debug:
print(t)
print("This is the",t ,"word of your list:",content[t])