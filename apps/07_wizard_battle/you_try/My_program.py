import random

from My_actors import Wizard, Creature

def main():
    print_header()
    game_loop()


def print_header():
    print('-----------------------')
    print('    WIZARD GAME APP')
    print('-----------------------')
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    # print(creatures)


    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'.format(active_creature.name, active_creature.level))
        print()


        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            hero.attack(active_creature)
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK, you want to leave the game. Bye, bye!')
            break


if __name__ == '__main__':
    main()
