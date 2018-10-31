# implementation of card game - Memory

import simplegui
import random

deck1 = [0,1,2,3,4,5,6,7]
deck2 = [0,1,2,3,4,5,6,7]
cards = deck1 + deck2
random.shuffle(cards)
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    a = pos[0] // 50
    exposed[a] = True
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global b
    for card_index in range(len(cards)):
        if exposed[card_index] == True:
            card_pos = 10+(50 * card_index)
            canvas.draw_text(str(cards[card_index]), [card_pos, 60], 50, "White")
        elif exposed[card_index] == False:
            canvas.draw_polygon([(50 * card_index, 0), (50 * card_index, 100), (50+(50 * card_index), 100), (50+(50 * card_index), 0)], 1, 'Brown', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric