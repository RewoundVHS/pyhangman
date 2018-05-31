#! /usr/bin/env python3

import hangmanart
from wordlist import words
import random

findWord = words[random.randrange(len(words))]
hidden = list('_' * len(findWord))

wrongCount = 0
maxWrong = 7

print(hangmanart.art[wrongCount])
print(''.join(hidden))

while((findWord != ''.join(hidden)) and (wrongCount < maxWrong)):
    enteredChar = input('Enter a character: ').lower()

    if enteredChar not in findWord:
        wrongCount += 1
        print('The letter', enteredChar, 'is not in the word')

    for i, c in enumerate(findWord):
        if c == enteredChar:
            hidden[i] = enteredChar

    print(hangmanart.art[wrongCount])
    print(''.join(hidden))

print('The word was', findWord)
if findWord == ''.join(hidden):
    print('You win!')
else:
    print('Better luck next time!')
