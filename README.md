# D-s-Pizza-
Pygame

#Set up Game
#Load game type cd Derek_loves_pizza_directory first 
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
WINDOW_RES =(WINDOW_WIDTH, WINDOW_HEIGHT)

#define tile parameters
WIDTH = 100
HEIGHT = 100

#define colors
WHITE =(255, 255, 255)

#------------------------------------------------------
#Load assets

#Create window
GAME_WINDOW = display.set_mode((WINDOW_RES))
display.set_caption('Derek Destroys Vampire Pizzas!')

#Background Image

background_img = image.load('restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, WINDOW_RES)

#Background grid
tile_color = WHITE
for row in range(6):
    for column in range(11):
        draw.rect(BACKGROUND, tile_color,(WIDTH* column,
                                      HEIGHT* row, WIDTH, HEIGHT), 1)


#Loading images
pizza_img = image.load('vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))
GAME_WINDOW.blit(BACKGROUND, (0,0))
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


