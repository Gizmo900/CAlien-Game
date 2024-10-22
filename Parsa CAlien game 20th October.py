# Parsa CAlien Game 20 Oct 2024

import pgzrun 
from random import randint


# Game window settings 
TITLE="Alien game"
WIDTH= 500
HEIGHT= 500


#create the alien actor and set initial position
alien= Actor ("calien")
alien.pos= 100,100
                     # The X-coordinate (100) represents the distance from the left side of the screen.
                     # The Y-coordinate (100) represents the distance from the top of the screen.
        
# Empty message to display
message= ""


# Function to draw everything on the screen 
def draw():
    screen.clear() # Clear the screen
    screen.fill("blue")  #Fill the backround with blue
    alien.draw()  #  draw the alien on the screen 
    screen.draw.text(message,center = (250,10), fontsize= 30,color="white")

#Function that runs when the mouse is clicked
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos): # if the alien is clicked 
        alien.pos= randint(50,450), randint (50,450) # Move the alien to a new random position 
        message= "Good shot!"  # change the message to good shot
    else:
        message= "You missed! Ha,Ha" # Change the message to You missed! HA ,HA

# start the game. 
pgzrun.go()




















