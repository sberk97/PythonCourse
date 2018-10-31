# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global times
    times = 7
    print "You have 7 guesses"
    secret_number=random.randrange(0,99)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global times
    times = 7
    print "You have 7 guesses"
    secret_number=random.randrange(0,99)   
    print "Restarting the game, range now is[0,100)"

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global times
    times = 10
    print "You have 10 guesses"
    secret_number=random.randrange(0,999)
    print "Restarting the game, range now is[0,1000)"
    
def input_guess(guess):
    # main game logic goes here	
    guess=int(guess)
    print "Guess was %s" % (guess)
    if guess==secret_number:
        print "Correct"
        new_game()
    elif guess > secret_number:
        print "Lower"
        global times
        if times > 0:
            times -= 1
            print "You have %s guesses left" % (times)
        else:
            print "You are out of guesses, the secret number was %s, new game begins" % (secret_number)
            new_game()
    elif guess < secret_number:
        print "Higher"
        if times > 0:
            times -= 1
            print "You have %s guesses left" % (times)
        else:
            print "You are out of guesses, the secret number was %s, new game begins" % (secret_number)
            new_game()
    else:
        print "Error"
    
# create frame
frame=simplegui.create_frame("Guess game", 300, 300)
input=frame.add_input("Input", input_guess, 50)
# register event handlers for control elements and start frame
button1=frame.add_button("Range is [0,100)", range100, 100)
button2=frame.add_button("Range is [0,1000)", range1000, 100)
frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
