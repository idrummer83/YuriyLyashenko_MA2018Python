# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# rock = 0
# Spock = 1
# paper = 2
# lizard = 3
# scissors = 4

# helper functions

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'incorrect name'

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'please set the number from 0 to 4'

    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    pass

    # print a blank line to separate consecutive games
    print(' ')

    # print out the message for the player's choice
    print('Plауеr chооsеs ' + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print('computer\'s choice ' + comp_choice)

    # compute difference of comp_number and player_number modulo five
    diff = (player_number - comp_number )%5

    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        return print('player computer draw')
    elif diff == 3 or diff == 4:
        return print('Cоmputеr wins!')
    elif diff == 2 or diff == 1:
        return print('Plауеr wins!')


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
