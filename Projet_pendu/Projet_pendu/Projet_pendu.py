import os


word = "hello"
word1=[]

word = input("Enter the secret word ")
word2 = ['a']

for i in range(0, len(word)):
    word1.append(word[i])

while len(word) > len(word2):
    word2.append("a")

print(word1)
print(word2)
#os.system('cls')


while word1 != word2 :
    letter = input("Enter a letter ")
    for c in range(0, len(word1)):
        if letter == word1[c]:
            word2[c] = letter
        print(word1)
        print(word2)
