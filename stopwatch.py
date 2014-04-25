# template for "Stopwatch: The Game"
import simplegui
# define global variables
interval = 100
time =0
tries=0
correct=0
tenths=0
running=False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t): 
    global tenths
    tenths=t%10
    seconds = (t/10)%60
    minutes= t/600
    if seconds>9:
        return str(minutes)+":"+str(seconds)+"."+str(tenths)
    else:
        return str(minutes)+":0"+str(seconds)+"."+str(tenths)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running=True

def stop():
    global tries, correct, tenths, running
    timer.stop()
    if running:
        if tenths==0:
            correct+=1
        tries+=1
    running = False
    
    

def reset():
    global time, tries, correct
    timer.stop()
    time=0
    tries=0
    correct=0
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time+=1


# define draw handler
def draw(canvas):
    global time
    canvas.draw_text(format(time), (60,100) , 34, "White")
    canvas.draw_text(str(correct), (155,30) , 21, "Green")
    canvas.draw_text("/", (167,30) , 21, "Green")
    canvas.draw_text(str(tries), (175,30) , 21, "Green")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch - The Game", 200, 200)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# start frame
frame.start()
reset()


# Please remember to review the grading rubric