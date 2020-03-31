# Set up Game
# Load game type cd Derek_loves_pizza_directory first
# Import libraries
import pygame
from pygame import *
from random import randint

# initialize Pygame
pygame.init()

# ------------------------------------------------------
# Define constant variables

# Define the parameters of the game window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

# define tile parameters
WIDTH = 100
HEIGHT = 100

# define colors
WHITE = (255, 255, 255)

#Define SPAWN_RATE
SPAWN_RATE = 360

# ------------------------------------------------------
# Load assets

# Create window
GAME_WINDOW = display.set_mode((WINDOW_RES))
display.set_caption('Derek Destroys Vampire Pizzas!')

# Background Image

background_img = image.load('C:\\Users\\hyamy\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, WINDOW_RES)

# Background grid
tile_color = WHITE
for row in range(6):
    for column in range(11):
        draw.rect(BACKGROUND, tile_color, (WIDTH * column,
                                           HEIGHT * row, WIDTH, HEIGHT), 1)


# Loading images
pizza_img = image.load('C:\\Users\\hyamy\\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))
GAME_WINDOW.blit(BACKGROUND, (0, 0))


# -------------------------------------------------------
# Set up Classes for Sprite

# Create a subclass of Sprite called VampireSprite


class VampireSprite(sprite.Sprite):
    # Define the VampireSprite set-up method
    def __init__(self):
        # Take all the behavior rules from Sprite class & use them
        super().__init__()
        # Set the default movement speed
        self.speed = 2
        # Randomly Select a lane between 0 and 4
        self.lane = randint(0, 4)
        # Add all the vampire pizza sprites to a group
        all_vampires.add(self)
        # Use the Vampire_pizza image
        self.image = VAMPIRE_PIZZA.copy()
        # Set each sprite's y-coordinate at the middle of lane
        y = 50 + self.lane * 100
        # Create a rect for each sprite and place it just
        # off the  right side of the screen in the correct lane
        self.rect = self.image.get_rect(center=(1100, y))

    def updates(self, game_window):
        game_window.blit(self.image, (self.rect.x, self.rect.y))

# -------------------------------------------------------
# Create class instances and groups
all_vampires = sprite.Group()
# -------------------------------------------------------
# Start main game loop

# Game loop
game_running = True
while game_running:


    # -------------------------------------------------------
    # Check for events

    # Checking for and handling events
    for event in pygame.event.get():

        # Exit Loop on quit
        if event.type == QUIT:
            game_running = FALSE

    #Spawn vampire pizza sprites
    if randint(1, SPAWN_RATE) == 1:
        VampireSprite()
# -------------------------------------------------------
            # update display

        for vampire in all_vampires:
            vampire.update(GAME_WINDOW)

        display.update()

# End of main game loop

# -------------------------------------------------------

# Clean up game
pygame.quit()


