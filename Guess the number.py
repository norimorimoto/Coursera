# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 0
num_range = 100
guesses_left = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used
    global secret_number
    global num_range
    global guesses_left
    
    # reset the secret number
    secret_number = random.randrange(0, num_range)
    
    # select guesses left
    if num_range == 100:
        guesses_left = 7
    elif num_range == 1000:
        guesses_left = 10
    
    # tell the player a new game has started
    print "New game. Range is from 0 to ", num_range, "."
    print "Number of remaining guesses is ", guesses_left, ". \n"
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guesses_left
    global secret_number
    
    # convert player input into integer
    player_guess = int(guess)
    
    # keep track of how many guesses are left
    guesses_left -= 1
    
    # if the player runs out of guesses, a new game starts
    if guesses_left == 0:
        print "Out of guesses \n"
        new_game()
    else:    
        print "Guess was " + str(player_guess)
        print "Number of remaining guesses is ", guesses_left
    
        if player_guess == secret_number:
            print "Correct! \n"
            new_game()
    
        elif player_guess > secret_number:
            print "Lower! \n"
    
        elif player_guess < secret_number:
            print "Higher! \n"
        
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter your guess", input_guess, 200)

# call new_game 
new_game()



# always remember to check your completed program against the grading rubric
