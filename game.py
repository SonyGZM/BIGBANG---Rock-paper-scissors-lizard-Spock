
import random
from termcolor import colored

options = ('rock', 'paper', 'scissors', 'lizard', 'spock')

computer_wins = 0
user_wins = 0

rounds = 1

name = input("What's your name? -> ", )

while True:
    print(' ' * 10)
    print('*' * 30)
    print('ROUND', rounds)
    print('--' * 15)

    print('Computer wins -> ', computer_wins)
    print(name, 'Wins -> ', user_wins)
    print(' ' * 10)

    user_option = input('Choose an option: rock, paper, scissors, lizard, spock -> ')
    user_option = user_option.lower()
    print(' ' * 10)

    if not user_option in options:
        print('Invalid answer')
        continue

    computer_option = random.choice(options)
    
    print('user decision -> ', user_option)
    print('computer decision ->', computer_option)
    print(' ' * 10)
   
    if user_option == computer_option:
        print('Tie!')
    
    
    # rock
    elif user_option == 'rock':
        if computer_option == 'paper':
            print('Paper cover stone')
            print('Computer win!')
            computer_wins += 1
        if computer_option == 'scissors':
            print('Rock breaks scissor')
            print(name, 'win!')
            user_wins += 1
        if computer_option == 'lizard':
            print('Rock crushes lizard')
            print(name, 'win!')
            user_wins += 1
        if computer_option == 'spock':
            print('Spock vaporizes stone')
            print('computer win!')
            computer_wins += 1

    # paper
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('Paper covers stone')
            print(name, 'win!')
            user_wins += 1
        if computer_option == 'scissors':
            print('Scissors cut paper')
            print('computer win!')
            computer_wins += 1
        if computer_option == 'lizard':
            print('Lizard devours paper')
            print('computer win!')
            computer_wins += 1
        if computer_option == 'spock':
            print('Paper overrules spock')
            print(name, 'win!')
            user_wins += 1

    # scissors
    elif user_option == 'scissors':
        if computer_option == 'rock':
            print('Rock breaks scissor')
            print('computer win!')
            computer_wins += 1
        if computer_option == 'paper':
            print('Scissors cut paper')
            print(name, 'win!')
            user_wins += 1
        if computer_option == 'lizard':
            print('Scissors decapitates lizard')
            print(name, 'win!')
            user_wins += 1
        if computer_option == 'spock':
            print('Spock breaks scissors')
            print('computer win!')
            computer_wins += 1

    # lizard
    elif user_option == 'lizard':
        if computer_option == 'rock':
            print('Rock crushes lizard')
            print('computer win!')
            computer_wins += 1
        if computer_option == 'paper':
            print('Lizard devours paper')
            print(name, 'win!')
            user_wins += 1
        if computer_option == 'scissors':
            print('Scissors decapitates lizard')
            print('computer win!')
            computer_wins += 1
        if computer_option == 'spock':
            print('Lizard poisons spock')
            print(name, 'win!')
            user_wins += 1
    
    # spock
    elif user_option == 'spock':
        if computer_option == 'rock':
            print('Spock vaporizes stone')
            print('computer win!')
            computer_wins += 1
        if computer_option == 'paper':
            print('Paper overrules spock')
            print('Computer win!')
            computer_wins += 1
        if computer_option == 'scissors':
            print('Spock breaks scissors')
            print(name, 'win!')
            user_wins += 1
        if computer_option == 'lizard':
            print('Lizard poisons spock')
            print(name, 'win!')
            user_wins += 1

    if computer_wins == 3:
        print('Computer win! 3 rounds! Thanks for play')
        break

    if user_wins == 3:
        print(name, 'win! 3 rounds! Thanks for play')
        break
        
    rounds += 1
