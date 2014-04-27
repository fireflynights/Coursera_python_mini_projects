# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1=0
score2=0


# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos=[0,0]
ball_vel= [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[300,200]
    if direction=='RIGHT':
        ball_vel = [random.randrange(120, 240)/60, -random.randrange(60, 180)/60]
    else:
        ball_vel=[-random.randrange(120, 240)/60,-random.randrange(60, 180)/60]
        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=150
    paddle2_pos=150
    paddle1_vel=0
    paddle2_vel=0
    score1=0
    score2=0
    spawn_ball('RIGHT')
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    #print ball_pos
    
    if (ball_pos[1]>=(HEIGHT-1)-BALL_RADIUS) or (ball_pos[1]<=0+BALL_RADIUS):#Ball hits top or bottom
        ball_vel[1]=-ball_vel[1] 
    elif ball_pos[0]<=PAD_WIDTH+BALL_RADIUS: #Ball hits left gutter
        if ball_pos[1]>=paddle1_pos and ball_pos[1]<=paddle1_pos+PAD_HEIGHT:# Ball hits left paddle
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]*=1.1
            ball_vel[1]*=1.1
        else:
            spawn_ball('RIGHT') 
            score2+=1
            
    elif ball_pos[0]>=(WIDTH-PAD_WIDTH-1)-BALL_RADIUS:#Ball hits right gutter
        if ball_pos[1]>=paddle2_pos and ball_pos[1]<=paddle2_pos+PAD_HEIGHT:# Ball hits left paddle
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]*=1.1
            ball_vel[1]*=1.1
        else: 
            spawn_ball('LEFT') 
            score1+=1
            
    
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos+paddle1_vel>0 and paddle1_pos+paddle1_vel<=HEIGHT-PAD_HEIGHT:
        paddle1_pos += paddle1_vel
 
    if paddle2_pos+paddle2_vel>0 and paddle2_pos+paddle2_vel<=HEIGHT-PAD_HEIGHT:    
        paddle2_pos += paddle2_vel
        
    # draw paddles
    canvas.draw_line([0,paddle1_pos],[0,paddle1_pos+PAD_HEIGHT], PAD_WIDTH*2, "White")
    canvas.draw_line([WIDTH,paddle2_pos],[WIDTH,paddle2_pos+PAD_HEIGHT], PAD_WIDTH*2, "White")
    # draw scores
    canvas.draw_text(str(score1), (120,100) , 34, "White")
    canvas.draw_text(str(score2), (450,100) , 34, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    accel=3
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= accel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel +=accel
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= accel
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += accel
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    accel=3
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel += accel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel -=accel
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel += accel
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= accel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)


# start frame
new_game()
frame.start()
