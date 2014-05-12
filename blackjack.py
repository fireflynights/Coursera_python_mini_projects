# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]	# create Hand object

    def __str__(self):   # return a string representation of a hand
        string_hand = ""
        #print len(self.hand)
        for i in range(len(self.hand)):
            #print i, self.hand[i]
            string_hand += str(self.hand[i]) + ' '
        return 'Hand Contains '+string_hand	
  

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
        hand_value=0
        ace_found=False
        string_hand=''
        for i in range(len(self.hand)):
            string_hand += str(self.hand[i]) + ' '
        
        if 'A' in string_hand:
            ace_found=True
        #print str(self.hand)
        for i in range(len(self.hand)):
             card_value=str(self.hand[i])
             card_value=card_value[1:]
             #print 'hand_value',hand_value
             hand_value+=VALUES[card_value]
        if ace_found:
            if hand_value+10<=21:
                hand_value+=10
             
        return hand_value
   
    def draw(self, canvas, pos):
        for c in self.hand:
            c.draw(canvas,  pos)
            pos[0]+=CARD_SIZE[0]
        # draw a hand on the canvas, use the draw method for cards

            

# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]	# create a Deck object
        for suit in SUITS: 
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
    # create a Card object using Card(suit, rank) and add it to the card list for the deck  

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        string_deck = ""
        for i in range(len(self.deck)):
            string_deck += str(self.deck[i]) + ' '
        return 'Deck Contains '+string_deck
    # return a string representing the deck
#define event handlers for buttons
def deal():
    global outcome, in_play,player_hand,dealer_hand,score,play_deck
    if not in_play:
        play_deck=Deck()
        play_deck.shuffle()
        player_hand=Hand()
        dealer_hand=Hand()
        #print play_deck
        for i in range(2):
            card = play_deck.deal_card()
            player_hand.add_card(card)
        for i in range(2):
            card = play_deck.deal_card()
            dealer_hand.add_card(card)    
        in_play = True
        outcome=''
    else:
        outcome='You lose'
        in_play= False
        score-=1
         

def hit():
    global outcome, in_play, player_hand,score,play_deck
    if in_play:
        player_hand.add_card(play_deck.deal_card())
        if player_hand.get_value()>21:
            outcome="You Busted!"
            in_play=False
            score-=1
        
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, player_hand,score,dealer_hand
    player_hand.get_value()
    if in_play:
        if outcome=="You Busted!":
            outcome ="Remember, you busted. New Deal?"
        else:
            while dealer_hand.get_value()<17:
                dealer_hand.add_card(play_deck.deal_card())    
            dealer_score=dealer_hand.get_value()
            if dealer_score>21:
                outcome="Dealer Busts! You win!"
                score+=1
            elif dealer_score<=21:
                if dealer_score>=player_hand.get_value():
                    outcome="Dealer wins!"
                    score-=1
                else:
                    outcome="You win!"
                    score+=1
        in_play=False 
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_hand, dealer_hand, score, outcome
    dealer_hand.draw(canvas, [100, 200])
    player_hand.draw(canvas, [100, 400])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [135,250], CARD_BACK_SIZE)
        canvas.draw_text('Hit or Stand?', (400, 370), 30, 'Black') 
    else:
        canvas.draw_text('New Deal?', (400, 100), 30, 'Black')
    
    canvas.draw_text('Dealer Hand', (100, 170), 30, 'Black')    
    canvas.draw_text('Player Hand', (100, 370), 30, 'Black')    
    score_text='Score:  '+ str(score)
    canvas.draw_text(score_text, (100, 100), 30, 'Black') 
    canvas.draw_text(outcome, (300, 50), 30, 'Black') 
    canvas.draw_text('Blackjack!', (100, 50), 30, 'Black') 

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric