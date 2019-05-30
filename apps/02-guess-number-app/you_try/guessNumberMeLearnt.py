"""The code I learnt from the video Guess number"""

import random

print('------------------------------')
print('      GUESS THE NUMBER APP')
print('------------------------------')
print()

number = random.randint(0, 100)
guess = -1 # -1 arvo varmistaa ettei lähtöarvona ole koskaan voittava arvo.

name = input('Player what is your name? ')

while True:
    guess = input('Guess a number between 0 and 100: ') # Kirjoittaessa saat tyypin selville sis. print(type(guess))
    guess = int(guess_text)
    # while loopin sisäisen tekstin saa sisennettyä valinnalla ja täbillä
    if guess < number:
        print('Sorry {}, but {} is LOWER than the number'.format(guess, name))

    elif guess > number:
        print('Sorry, but {} is HIGHER than the number'.format(guess))

    else:
        print('Excellent work {}, you won, it was {}!'.format(name, guess))
        break

print('done')