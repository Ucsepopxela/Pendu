import os
guessed = []
copy = 0
word = "hello"
word1=[]
tmp= "test"
word = input("Enter the secret word ")
word2 = ['_']
fautes = 0
guessed = []
#création des deux listes représentant le mot mystère (liste mot et liste vide de même longueur)
for i in range(0, len(word)):
    word1.append(word[i])

while len(word) > len(word2):
    word2.append("_")

#print(word1)
#print(word2)
os.system('cls')


while word1 != word2 and fautes <=6:
    h = 0
    letter = input("Enter a letter ")
    for u in range(0, len(guessed)):
        if guessed[u] == letter:
            copy = 1
            

    
    if copy == 0:
        for c in range(0, len(word1)):
            if letter == word1[c]:
                word2[c] = letter
                h +=1

        
        if h == 0:
            fautes +=1
        guessed.append(letter)


    os.system('cls')





    
    print("You have the right to make ", 6-fautes, " more mistakes.")
    print("Letters you have guessed : ", " ".join(guessed))
    print("Number of mistakes : ", fautes,)
    tmp = " ".join(word2)
    print(tmp)

    if copy !=0:
        print("You've already guessed that letter !")
    copy = 0


if fautes == 7:
    print("You lost....")
elif fautes < 6 :
    print("Well done. You found '",word, "'")