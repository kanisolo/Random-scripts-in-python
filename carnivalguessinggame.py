"""
Creation of the carnival guessing game
"""

from random import shuffle

mylist = [' ','O',' ']

def shuffle_list(mylist):
    shuffle(mylist)

    return mylist

# print(shuffle_list(mylist))

def player_guess():

    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Pick a number : 0, 1 or 2: ")
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)

#shuffle the list
mixedup_list = shuffle_list(mylist)

#Get user's guess
guess = player_guess()

#Ceheck user's guess
check_guess(mixedup_list, guess)
