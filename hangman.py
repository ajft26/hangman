#By AJFT 21/02/2021
from words import word_list
import random
import os
import time

os.system('cls')
print('\n')
#1. draw the gallow
def hang1():
    print('             ---------')
    print('             |',)
    print('             |',)
    print('             |',)
    print('             |',)
    print('             |',)
    print('             |',)

def hang2():
    print('             ---------')
    print('             |       |')
    print('             |',)
    print('             |',)
    print('             |',)
    print('             |',)
    print('             |',)

def hang3():
    print('             ---------')
    print('             |       |')
    print('             |       O')
    print('             |',)
    print('             |',)
    print('             |',)
    print('             |',)

def hang4():
    print('             ---------')
    print('             |       |')
    print('             |       O')
    print('             |       |')
    print('             |',)
    print('             |',)
    print('             |',)

def hang5():
    print('             ---------')
    print('             |       |')
    print('             |       O')
    print('             |       |')
    print('             |       |')
    print('             |',)
    print('             |',)

def hang6():
    print('             ---------')
    print('             |       |')
    print('             |       O')
    print('             |       |/')
    print('             |       |')
    print('             |',)
    print('             |',)

def hang7():
    print('             ---------')
    print('             |       |')
    print('             |       O')
    print('             |      \|/')
    print('             |       |')
    print('             |',)
    print('             |',)

def hang8():
    print('             ---------')
    print('             |       |')
    print('             |       O')
    print('             |      \|/')
    print('             |       |')
    print('             |      /')
    print('             |',)

def hang9():
    print('             ---------')
    print('             |       |')
    print('             |       O')
    print('             |      \|/')
    print('             |       |')
    print('             |      / \\')
    print('             |',)

def printListEmpty():
    for x in range(len(listEmpty)):
        print(listEmpty[x],end='')

hangs = {'hang2':hang2,'hang3':hang3, 'hang4':hang4,'hang5':hang5, 'hang6':hang6,'hang7':hang7, 'hang8':hang8, 'hang9':hang9}

random.shuffle(word_list)
word = random.choice(word_list)
 #input('Write down a word: ')
os.system('cls')
listWord = list(word.upper())
listEmpty= []
guessedWords = []

#fill the list empty with underscore
for i in range(len(listWord)):
    listEmpty.append('_ ')
#End fill the list empty with underscore

funcExecute = hang1
funcExecute()

i=2
while i < 10:
    print('\n')

    #print on the screen the listEmpty
    printListEmpty()


    letter = input('\nPlease, guess a letter: ')
    os.system('cls')

    if letter.upper() in guessedWords:
        os.system('cls')
        funcExecute()
        print('You already guessed the letter ',letter.upper())
    else:
        guessedWords.append(letter.upper())



        #look for the letter in the listWord if it is found it it will be replaced in the same position in listEmpty
        encuentra = False
        for letra in range(len(listWord)):
            if listWord[letra] == letter.upper():
                listEmpty[letra] = letter.upper()
                encuentra = True

        #Join the list to string to compare them. If they are equals the guest player won!!!
        if ("".join(listWord) == "".join(listEmpty)):
            funcExecute()
            printListEmpty()
            print('\nThe hidden word was {}'.format("".join(listWord)))
            print('\nYou won. Congrats!!!!. ')
            time.sleep(5)
            break

        #if the letter is not in the listWord the hangman starts appearing step by step, for any wrong letter
        if encuentra == False:
            xhang= 'hang'+str(i)
            if xhang in hangs:
                funcExecute = hangs[xhang]
                funcExecute()
                i = i + 1
            else:
                funcExecute()
        else:
            funcExecute()

        # if i equals 10 the man was hung completely, after 10 wrongs letters
        if i == 10:
            print("\5 YOU WERE HUNG...The correct word was {}. Try again, please... \5".format("".join(listWord)) )
