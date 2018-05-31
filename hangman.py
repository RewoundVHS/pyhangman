#! /usr/bin/env python3

import hangmanart
from wordlist import words
import random

findWord = words[random.randrange(len(words))]
hidden = list('_' * len(findWord))

wrongCount = 0
maxWrong = 7

guessed = False

print(hangmanart.art[wrongCount])
print(''.join(hidden))

while((findWord != ''.join(hidden)) and (wrongCount < maxWrong) and not guessed):
    enteredChar = input('Enter a letter or ! to solve: ').lower()

    if enteredChar.isalpha() and len(enteredChar) == 1:
        if enteredChar not in findWord:
            wrongCount += 1
            print('The letter', enteredChar, 'is not in the word')

        for i, c in enumerate(findWord):
            if c == enteredChar:
                hidden[i] = enteredChar

        print(hangmanart.art[wrongCount])
        print(''.join(hidden))

    elif enteredChar == '!':
        guess = input('Enter your guess: ').lower()
        hidden = list(guess)
        guessed = True

    else:
        print('Please enter a letter')

if findWord == ''.join(hidden):
    print('You win!')
else:
    print('The word was', findWord)
    print('Better luck next time!')
