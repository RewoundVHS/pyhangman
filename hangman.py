#! /usr/bin/env python3

import hangmanart
from wordlist import words
import random

findWord = words[random.randrange(len(words))]
hidden = list('_' * len(findWord))
wrongLetters = list('')

wrongCount = 0
maxWrong = 7

guessed = False

print(hangmanart.art[wrongCount])
print(''.join(hidden))

# Prompt for letters while the player has not found the word, has not gotten
# more than the maximum wrong and has not put in their final guess
while((findWord != ''.join(hidden)) and (wrongCount < maxWrong) and not guessed):
    enteredChar = input('Enter a letter or ! to solve: ').lower()

    # Validate char
    if enteredChar.isalpha() and len(enteredChar) == 1:
        if enteredChar not in findWord:
            print('The letter', enteredChar, 'is not in the word')
            wrongCount += 1
            wrongLetters.append(enteredChar)

        # Replace underscores with found chars
        for i, c in enumerate(findWord):
            if c == enteredChar:
                hidden[i] = enteredChar

        # Print game elements
        print(hangmanart.art[wrongCount])
        print(''.join(hidden))
        if len(wrongLetters) > 0:
            print('You have incorrectly guessed:', wrongLetters)

    # Prompt for final guess
    elif enteredChar == '!':
        guess = input('Enter your guess: ').lower()
        hidden = list(guess)
        guessed = True

    # Handle non-alpha and more than one char
    else:
        print('Please enter a letter')

# Determine if player won or lost
if findWord == ''.join(hidden):
    print('You win!')
else:
    print('The word was', findWord)
    print('Better luck next time!')
