import os
import random

CurrDir = os.getcwd()
os.chdir(CurrDir)


k = "y"
while k == "y":
    guessed = []
    copy = 0
    word = "hello"
    word1 = []
    tmp = "test"

    with open("words.txt") as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    print(content)
    t = random.randint(0, len(content)-1))
    # Debug:
    print(t)

    word = content[t]
    word2 = ['_']
    fautes = 0
    guessed = []
    # création des deux listes représentant le mot mystère (liste mot et liste vide de même longueur)
    for i in range(0, len(word)):
        word1.append(word[i].lower())

    while len(word) > len(word2):
        word2.append("_")

    # print(word1)
    # print(word2)
    os.system('cls')

    sex = input("Choose the sex of the character (M or F) : ")
    sex = sex.lower()
    if sex != "m" and sex != "f":
        print("It is not a M or a F !!!")
    elif sex == "m":

        while word1 != word2 and fautes <= 6:
            h = 0
            letter = input("Enter a letter : ")

            if len(letter) == 1:  # checking that there is only one entered letter

                letter = letter.lower()
                for u in range(0, len(guessed)):
                    if guessed[u] == letter:
                        copy = 1  # checking if the letter has already been entered once

                if copy == 0:
                    for c in range(0, len(word1)):
                        if letter == word1[c]:
                            word2[c] = letter
                            h += 1  # replacing the "_" in word 2 by the actual letters

                    if h == 0:
                        fautes += 1  # mistakes counter

                    guessed.append(letter)

                os.system('cls')

                # Printing the results of each loop
                print("You have the right to make ", 6 - fautes, " more mistakes.")
                print("Letters you have guessed : ", " ".join(guessed))
                print("Number of mistakes : ", fautes, )
                tmp = " ".join(word2)
                print("Your word is :", tmp)

                if copy != 0:
                    print("You've already guessed that letter !")
                copy = 0
                if fautes == 7:
                    print("  ------")
                    print("  |    |")
                    print(" ( )   |")
                    print(" /|\   |")
                    print("/ | \  |")
                    print(" / \   |")
                    print("/   \  |")
                    print("    ___|___")

                if fautes == 6:
                    print("  ------")
                    print("  |    |")
                    print(" ( )   |")
                    print(" /|\   |")
                    print("/ | \  |")
                    print(" /     |")
                    print("/      |")
                    print("    ___|___")

                if fautes == 5:
                    print("  ------")
                    print("  |    |")
                    print(" ( )   |")
                    print(" /|\   |")
                    print("/ | \  |")
                    print("       |")
                    print("       |")
                    print("    ___|___")

                if fautes == 4:
                    print("  ------")
                    print("  |    |")
                    print(" ( )   |")
                    print(" /|    |")
                    print("/ |    |")
                    print("       |")
                    print("       |")
                    print("    ___|___")

                if fautes == 3:
                    print("  ------")
                    print("  |    |")
                    print(" ( )   |")
                    print("  |    |")
                    print("  |    |")
                    print("       |")
                    print("       |")
                    print("    ___|___")

                if fautes == 2:
                    print("  ------")
                    print("  |    |")
                    print(" ( )   |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("    ___|___")

                if fautes == 1:
                    print("  ------")
                    print("  |    |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("    ___|___")
            else:
                print("You must write only ONE letter !")

                # printing the final results
    else:
        while word1 != word2 and fautes <= 6:
            h = 0
            letter = input("Enter a letter :")

            if len(letter) == 1:  # checking that there is only one entered letter

                letter = letter.lower()
                for u in range(0, len(guessed)):
                    if guessed[u] == letter:
                        copy = 1  # checking if the letter has already been entered once

                if copy == 0:
                    for c in range(0, len(word1)):
                        if letter == word1[c]:
                            word2[c] = letter
                            h += 1  # replacing the "_" in word 2 by the actual letters

                    if h == 0:
                        fautes += 1  # mistakes counter

                    guessed.append(letter)

                os.system('cls')

                # Printing the results of each loop
                print("You have the right to make ", 6 - fautes, " more mistakes.")
                print("Letters you have guessed : ", " ".join(guessed))
                print("Number of mistakes : ", fautes, )
                tmp = " ".join(word2)
                print("Your word is :", tmp)

                if copy != 0:
                    print("You've already guessed that letter !")
                copy = 0
                if fautes == 7:
                    print("  ------")
                    print("  |    |")
                    print(" { }   |")
                    print(" /|\   |")
                    print("/ | \  |")
                    print(" / \   |")
                    print("/---\  |")
                    print(" | |   |")
                    print("    ___|___")

                if fautes == 6:
                    print("  ------")
                    print("  |    |")
                    print(" { }   |")
                    print(" /|\   |")
                    print("/ | \  |")
                    print(" / \   |")
                    print("/---\  |")
                    print(" |     |")
                    print("    ___|___")

                if fautes == 5:
                    print("  ------")
                    print("  |    |")
                    print(" { }   |")
                    print(" /|\   |")
                    print("/ | \  |")
                    print("       |")
                    print("       |")
                    print("    ___|___")

                if fautes == 4:
                    print("  ------")
                    print("  |    |")
                    print(" { }   |")
                    print(" /|    |")
                    print("/ |    |")
                    print("       |")
                    print("       |")
                    print("    ___|___")

                if fautes == 3:
                    print("  ------")
                    print("  |    |")
                    print(" { }   |")
                    print("  |    |")
                    print("  |    |")
                    print("       |")
                    print("       |")
                    print("    ___|___")

                if fautes == 2:
                    print("  ------")
                    print("  |    |")
                    print(" { }   |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("    ___|___")

                if fautes == 1:
                    print("  ------")
                    print("  |    |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("       |")
                    print("    ___|___")
                else:
                    print("You must write only ONE letter")

    if fautes == 7:
        print("You lost.... The word was :", word)
    elif fautes <= 6:
        print("Well done. You found '", word, "'")

    k = input("Do you want to replay ? Y or N : ")
    k = k.lower()

