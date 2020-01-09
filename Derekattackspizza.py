#Set up Game

#Import libraries 
import pygame
from pygame import *

#initialize Pygame
pygame.init()

#------------------------------------------------------
#Define constant variables

#Define the parameters of the game window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#------------------------------------------------------
#Load assets

#Create window
GAME_WINDOW = display.set_mode((WINDOW_RES))
display.set_caption('Derek Destroys Vampire Pizzas!')

#Loading images
pizza_img = image.load('vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900, 400))


#-------------------------------------------------------
#Start main game loop

#Game loop
game_running = True
while game_running:

#-------------------------------------------------------    
#Check for events

#Checking for and handling events
    for event in pygame.event.get():

#Exit Loop on quit
        if event.type == QUIT:
            game_running = FALSE

#-------------------------------------------------------
            #update display
        display.update()

#End of main game loop

#-------------------------------------------------------

#Clean up game
pygame.quit()
