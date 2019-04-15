"""My try on Guess number app"""

import random

print('------------------------------')
print('      GUESS THE NUMBER APP')
print('------------------------------')
print()

number = random.randint(0, 100)

while True:
    guess = input('Guess a number between 0 and 100: ')
    guess = int(guess)
    if guess < number:
        print('Sorry, but ' + str(guess) + ' is LOWER than the number')

    if guess > number:
        print('Sorry, but ' + str(guess) + ' is HIGHER than the number')

    if guess == number:
        break

print("YES! You've got it. The number was " + str(number))
