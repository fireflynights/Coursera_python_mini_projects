# implementation of card game - Memory

import simplegui
import random
state=0
firstcard=0
secondcard=0
turns=0

# helper function to initialize globals
def new_game():
    global new_deck,exposed,turns,state,firstcard,secondcard
    new_deck=range(8)+range(8) #sets up pairs 0-7
    random.shuffle(new_deck)
    exposed=[False for n in range(16)] #sets all cards facedown
    turns=0
    firstcard=0
    secondcard=0
    state=0

    
# define event handlers
def mouseclick(pos):
    '''state of 0 is beginning of game, state of 1 means 1 card 
is up, state of 2 means 2 cards are up, checks if match. 
on all states checks first if card is already exposed
before continuing'''
    global state,firstcard,secondcard,turns
    card=pos[0]//50
    if state == 0:
        exposed[card]=True
        firstcard=card
        state=1
    elif state==1:
        if exposed[card]==False:
            exposed[card]=True
            secondcard=card
            turns+=1
            state=2 
    elif state==2:
        if exposed[card]==False:
            state=1
            exposed[card]=True
            if new_deck[firstcard]!=new_deck[secondcard]:
                exposed[firstcard]=False
                exposed[secondcard]=False
            firstcard=card
            turns+=1
            secondcard=0
                              
# cards are logically 50x100 pixels in size    
def draw(canvas):
    '''prints green card if face down and number on black background if face up'''
    global exposed, turns
    divider=50
    initial=0
    label.set_text("Turn = " + str(turns))
    for n in range(16):
        if exposed[n]==False:
            canvas.draw_polygon([(initial, 0), (initial+50, 0), (initial+50, 100), (initial,100)], 1,'Green', 'Green')
        else:
            canvas.draw_polygon([(initial, 0), (initial+50, 0), (initial+50, 100), (initial,100)], 1,'Black', 'Black')
            canvas.draw_text(str(new_deck[n]), (initial+18,60) , 34, "White")
        canvas.draw_line((initial,0), (initial,100), 1, 'Black')
        initial +=divider
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns=0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric