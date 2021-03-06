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


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_vel = [0, 0]
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(3, 5)
        ball_vel[1] = -1 * random.randrange(2, 5)
    elif direction == LEFT:
        ball_vel[0] = -1 * random.randrange(3, 5)
        ball_vel[1] = -1 * random.randrange(2, 5)

        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)
    paddle1_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle2_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle1_vel = 0
    paddle2_vel = 0


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'Yellow', 'Green')

    if (ball_pos[1] <= BALL_RADIUS or ball_pos [1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = -1 * ball_vel[1]
      
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= 0 and paddle1_pos + paddle1_vel <= (HEIGHT - PAD_HEIGHT):
        paddle1_pos += paddle1_vel
        
    if paddle2_pos + paddle2_vel >= 0 and paddle2_pos + paddle2_vel <= (HEIGHT - PAD_HEIGHT):
        paddle2_pos += paddle2_vel
        
    # draw paddles
    canvas.draw_polygon([[WIDTH, paddle1_pos], [(WIDTH - PAD_WIDTH), (paddle1_pos)], [(WIDTH - PAD_WIDTH), (paddle1_pos + PAD_HEIGHT)], [WIDTH, (paddle1_pos + PAD_HEIGHT)]], 1, 'Red', 'Red')
    canvas.draw_polygon([[0, paddle2_pos], [PAD_WIDTH, paddle2_pos], [PAD_WIDTH, (paddle2_pos + PAD_HEIGHT)], [0, (paddle2_pos + PAD_HEIGHT)]], 1, 'Blue', 'Blue')
    # determine whether paddle and ball collide    
    
    if (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)) and (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + PAD_HEIGHT):
        spawn_ball(RIGHT)
        score1 += 1
    elif (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)) and (ball_pos[1] >= paddle2_pos or ball_pos[1] <= paddle2_pos + PAD_HEIGHT):
        ball_vel[0] = -1.10 * ball_vel[0]
        
    if (ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS)) and (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + PAD_HEIGHT):
        spawn_ball(LEFT)
        score2 += 1
    elif (ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS)) and (ball_pos[1] >= paddle1_pos or ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
        ball_vel[0] = -1.10 * ball_vel[0]
      
    # draw scores
    canvas.draw_text(str(score2), (100, 50), 50, 'Blue')
    canvas.draw_text(str(score1), (470, 50), 50, 'Red')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel = -10
    elif key == simplegui.KEY_MAP['down']:
        paddle1_vel = 10
        
    if key == simplegui.KEY_MAP['w']:
        paddle2_vel = -15
    elif key == simplegui.KEY_MAP['s']:
        paddle2_vel = 15
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle1_vel = 0
        
    if key == simplegui.KEY_MAP['w']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
new_game_button = frame.add_button('New Game!', new_game, 100)

# start frame
new_game()
frame.start()
