# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# intialize globals

guess_number = 0
num_guesses = 7
past = 0

def new_secret():
    return random.randrange(0, 100)

secret_number = new_secret()


def input_guess(num):
    return int(num)

frame = simplegui.create_frame('Guess Number', 100, 200)
inp = frame.add_input('user_num', input_guess, 80)


def restart_new():
    restart(10)
    global past
    past = 10

    
def restart(*args):
    print('game RESTARTED')
    print('')
    inp.set_text('')    
    global secret_number
    global num_guesses
    if len(args) > 0:
        num_guesses = 10
        secret_number = random.randrange(0, 1000)
    else:
        num_guesses = 7
        secret_number = random.randrange(0, 100)

        
def remaining(*args):
    secret = secret_number
    guess = int(inp.get_text())
    print('Guess was ' + str(guess))
        
    global num_guesses
    if num_guesses >= 0:
        print('Number of remaining guesses is ' + str(num_guesses))
        num_guesses -= 1
    else:
        print('You ran out of guesses. The number was ' + str(secret_number))
        if past:
            restart_new()
        else:
            restart()
            
    mid = (secret + guess)//2
    if mid > secret and mid < guess:
        print('Lower!')
        print('#')
    elif mid < secret and mid > guess:
        print('Higher!')
        print('#')
    else:
        print('Correct!')
        if past:
            restart_new()
        else:
            restart()
        
frame.add_button("Rangeis[0,100)", restart, 120)
frame.add_button("Rangeis[0,1000)", restart_new, 120)
frame.add_button("Guess", remaining, 100) 
input_guess("50")


###################################################
# Start our test #1 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#input_guess("50")
#input_guess("75")
#input_guess("62")
#input_guess("68")
#input_guess("71")
#input_guess("73")
#input_guess("74")

###################################################
# Output from test #1
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Higher!
#
#Guess was 75
#Number of remaining guesses is 5
#Lower!
#
#Guess was 62
#Number of remaining guesses is 4
#Higher!
#
#Guess was 68
#Number of remaining guesses is 3
#Higher!
#
#Guess was 71
#Number of remaining guesses is 2
#Higher!
#
#Guess was 73
#Number of remaining guesses is 1
#Higher!
#
#Guess was 74
#Number of remaining guesses is 0
#Correct!
#
#New game. Range is [0,100)
#Number of remaining guesses is 7

###################################################
# Start our test #2 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#range1000()
#secret_number = 375    
#input_guess("500")
#input_guess("250")
#input_guess("375")

###################################################
# Output from test #2
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#New game. Range is [0,1000)
#Number of remaining guesses is 10
#
#Guess was 500
#Number of remaining guesses is 9
#Lower!
#
#Guess was 250
#Number of remaining guesses is 8
#Higher!
#
#Guess was 375
#Number of remaining guesses is 7
#Correct!
#
#New game. Range is [0,1000)
#Number of remaining guesses is 10



###################################################
# Start our test #3 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#range100()
#secret_number = 28 
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")

###################################################
# Output from test #3
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Lower!
#
#Guess was 50
#Number of remaining guesses is 5
#Lower!
#
#Guess was 50
#Number of remaining guesses is 4
#Lower!
#
#Guess was 50
#Number of remaining guesses is 3
#Lower!
#
#Guess was 50
#Number of remaining guesses is 2
#Lower!
#
#Guess was 50
#Number of remaining guesses is 1
#Lower!
#
#Guess was 50
#Number of remaining guesses is 0
#You ran out of guesses.  The number was 28
#
#New game. Range is [0,100)
#Number of remaining guesses is 7
