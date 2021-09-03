# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game

range_selector = random.randrange (0, 100)
guess_selector = 7

def new_game():
    # initialize global variables used in your code here
    global secret_number, range_selector, guesses_left, guess_selector
    secret_number = range_selector
    guesses_left = guess_selector
    print "New game! " + str(guesses_left) + " guesses left"
    print ""

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, range_selector, guess_selector
    range_selector = random.randrange (0, 100)
    guess_selector = 7
    print "Range is now 100!"
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game  
    global secret_number, range_selector, guess_selector
    range_selector = random.randrange (0, 1000)
    guess_selector = 10
    print "Range is now 1000!"
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guesses_left
    print "Guess was ", int(guess)
    guesses_left -= 1
    if guesses_left == 0:
        print "You lost!"
        print ""
        new_game()
    elif int(guess) == secret_number:
        print "Correct! You won!"
        print "---------------"
        print ""
        new_game()
    elif int(guess) > secret_number:
        print "Lower"
    elif int(guess) < secret_number:
        print "Higher"
    print str(guesses_left) + " guesses left.."
    print ""
    
# create frame
frame = simplegui.create_frame('Guess The Number!', 200, 200)

# register event handlers for control elements and start frame
inp = frame.add_input('Guess', input_guess, 100)
range100 = frame.add_button('Range 100', range100, 100)
range1000 = frame.add_button('Range 1000', range1000, 100)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
