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
init_pos= [WIDTH /2, HEIGHT /2]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH /2 ,HEIGHT / 2]
    ball_vel = [0, 2]
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(1, 5)
        ball_vel[1] = random.randrange(1, 5)
        ball_vel[1] = -ball_vel[1]
    if direction == "LEFT":
        ball_vel[0] = random.randrange(1, 5)
        ball_vel[1] = random.randrange(1, 5)
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball("LEFT")
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # odbicia pilki
    #lewa
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        ball_vel[0]= - ball_vel[0]
        spawn_ball("RIGHT")
    #prawa
    if ball_pos[0] >= (WIDTH - BALL_RADIUS) -PAD_WIDTH:
        ball_vel[0]= - ball_vel[0]
        spawn_ball("LEFT")
    #gora
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1]= - ball_vel[1]
    #dol
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1]= - ball_vel[1]
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
