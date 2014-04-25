# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables
num_range=100
secret_num=0
remaining_guesses=0

# helper function to start and restart the game
def new_game():
    '''starts a new game. sets secret_num to random number in given range.
    resets number of guesses'''
    global secret_num, remaining_guesses
    secret_num=random.randrange(0,num_range)
    print "\nNew Game. Range is 0 to", num_range
    if num_range==100:
        remaining_guesses=7
    else:
        remaining_guesses=10
    print "Number of remaining guesses is", remaining_guesses


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range=100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range=1000
    new_game()
    
def input_guess(guess):	
    '''checks the number of remaining guesses against secret number
    restarts game if player is out of guesses'''
    global remaining_guesses
    remaining_guesses-=1
    print "\nGuess was",guess
    print "Number of remaining guesses is",remaining_guesses
    if remaining_guesses!=0:
        if int(guess)<secret_num:
            print "Higher!"
        elif int(guess)>secret_num:
            print "Lower!"
        else:
            print "Correct!"
            new_game()
    else:
        print "Game over. Try again!"
        print "The number was:",secret_num
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the number!",200,200)


# register event handlers for control elements
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 100)

# call new_game and start frame

new_game()
frame.start()