# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # converts names to corresponding numbers
    if name=='rock':
        number= 0
    elif name=='Spock':
            number= 1
    elif name=='paper':
        number= 2
    elif name=='lizard':
        number= 3
    elif name=='scissors':
        number= 4
    else:
        number = 'unknown value'
    return number


def number_to_name(number):
    # convert numbers to corresponding names
    if number==0:
        name= 'rock'
    elif number==1:
            name= 'Spock'
    elif number==2:
        name='paper'
    elif number==3:
        name= 'lizard'
    elif number==4:
        name= 'scissors'
    else:
        name = 'unknown value'
    return name    
   
    

def rpsls(player_choice): 
    
    # print out the message for the player's choice
    print 'Player chooses ' + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice
    
    
   
   # compute difference of comp_number and player_number modulo five 
    winner=(comp_number-player_number) % 5
 
   # use if/elif/else to determine winner, print winner message
    if (winner == 1) or (winner ==2):
        print 'Computer wins!'
    elif (winner==3) or (winner==4):
        print 'Player wins!'
    else:
        print 'Player and Computer tie!'
    
    # print a blank line to separate consecutive games
    print '\n'
   
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


