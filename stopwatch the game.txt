# template for "Stopwatch: The Game"
import simplegui

# define global variables
# time in 0.1 sec intervals
t = 0
minutes = 0
seconds = 0
tenths = 0 
success = 0 
attempts = 0
wow = ""
boolean = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global minutes, seconds, tenths
    minutes = (t / 10) // 60 
    seconds = t / 10 - minutes * 60 
    tenths = t % 10
    return str(minutes) + ":" + str(seconds // 10) + str(seconds % 10) + "." + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global wow, boolean
    boolean = True
    timer.start()
    wow = ""
    
def stop():
    global tenths, success, attempts, wow, boolean
    timer.stop()
    if tenths == 0 and boolean:
        success += 1
        attempts += 1
        wow = "wow!"
        boolean = False
    elif boolean:
        attempts += 1
        wow = "close one!"
        boolean = False
    
def reset():
    global t, success, attempts
    timer.stop()
    t = 0
    success = 0
    attempts = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    
    
# define draw handler
def draw_handler(canvas):
    global minutes, seconds, tenths
    canvas.draw_text(format(t), [190, 250], 52, 'Red')
    canvas.draw_text(str(success) + "/" + str(attempts), [350, 100], 52, 'Red')
    canvas.draw_text(wow, [200, 400], 52, 'Red')

# create frame
frame = simplegui.create_frame('Stopwatch', 500, 500)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
start = frame.add_button('Start', start, 100)
stop = frame.add_button('Stop', stop, 100)
reset = frame.add_button('Reset', reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric
