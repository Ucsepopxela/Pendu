import os
import random
CurrDir = os.getcwd()
os.chdir(CurrDir)



with open("words.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

TO BE DONE !!!