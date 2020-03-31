# Set up Game
# Load game type cd Derek_loves_pizza_directory first
# Import libraries
import pygame
from pygame import *
from random import randint

# initialize Pygame
pygame.init()

# Setup Clock
clock = time.Clock()

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

# Define RATES
SPAWN_RATE = 360
FRAME_RATE = 60

# Set up Counters
STARTING_BUCKS = 15
BUCK_RATE = 120
STARTING_BUCK_BOOSTER = 1

# Set up Win/Lose conditions
MAX_BAD_REVIEWS = 3
WIN_TIME = FRAME_RATE * 60 * 3

# Define speeds
REG_SPEED = 2
SLOW_SPEED = 1

# ------------------------------------------------------
# Load assets

# Create window
GAME_WINDOW = display.set_mode((WINDOW_RES))
display.set_caption('Derek Destroys Vampire Pizzas!')

# Background Image

background_img = image.load(
    'C:\\Users\\hyamy\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, WINDOW_RES)


# Setting up Enemy images
pizza_img = image.load(
    'C:\\Users\\hyamy\\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))

# Setting up trap images
garlic_img = image.load(
    'C:\\Users\\hyamy\\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\Galaxy.jpg')
garlic_surf = Surface.convert_alpha(garlic_img)
GARLIC = transform.scale(garlic_surf, (WIDTH, HEIGHT))

cutter_img = image.load(
    'C:\\Users\\hyamy\\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\pizzacutter.png')
cutter_surf = Surface.convert_alpha(cutter_img)
CUTTER = transform.scale(cutter_surf, (WIDTH, HEIGHT))

pepperoni_img = image.load(
    'C:\\Users\\hyamy\\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\pepperoni.png')
pepperoni_surf = Surface.convert_alpha(pepperoni_img)
PEPPERONI = transform.scale(pepperoni_surf, (WIDTH, HEIGHT))

# -------------------------------------------------------
# Set up Class Objects

# Create a subclass of Sprite called VampireSprite


class VampireSprite(sprite.Sprite):
    # Define the VampireSprite set-up method
    def __init__(self):
        # Take all the behavior rules from Sprite class & use them
        super().__init__()
        # Set the default movement speed
        self.speed = REG_SPEED
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
        self.health = 100

    def update(self, game_window, counters):
        # Erase the last Sprite image
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
        # Move the Sprites
        self.rect.x -= self.speed
        if self.health <= 0 or self.rect.x <= 100:
            self.kill()
            if self.rect.x <= 100:
                counters.bad_reviews += 1
        else:
            # Update Sprite images to new location
            game_window.blit(self.image, (self.rect.x, self.rect.y))

# Apply trap effects to enemies
    def attacks(self, tile):
        if tile.trap == SLOW:
            self.speed = SLOW_SPEED
        if tile.trap == DAMAGE:
            self.health -= 1


# Create an object cor tracking the game state
class Counters(object):

    # Set up instances of counters

    def __init__(self, pizza_bucks, buck_rate, buck_booster, timer):
        self.loop_count = 0
        self.display_font = font.Font(
            'C:\\Users\hyamy\\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\pizza_font.ttf', 25)
        self.pizza_bucks = pizza_bucks
        self.buck_rate = buck_rate
        self.buck_booster = buck_booster
        self.bucks_rect = None
        self.timer = timer
        self.timer_rect = None
        self.bad_reviews = 0
        self.bad_rev_rect = None

# Set the rate that the player earns pizza bucks
     def increment_bucks(self:
        if self.loop_count % self.buck_rate == 0:
            self.pizza_bucks += self.buck_booster

    # Display pizza bucks total on the screen

    def draw_bucks(self, game_window):
        if bool(self.bucks_rect):
            game_window.blit(BACKGROUND, (self.bucks_rect.x,
                                          self.bucks_rect.y), self.bucks_rect)
        bucks_surf = self.display_font.render(
            str(self.pizza_bucks), True, WHITE)
        self.bucks_rect = bucks_surf.get_rect()
        self.bucks_rect.x = WINDOW_WIDTH - 50
        self.bucks_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(bucks_surf, self.bucks_rect)

    # Display bad reviews total on the screen

    def draw_bad_reviews(self, game_window):
        if bool(self.bad_rev_rect):
            game_window.blit(BACKGROUND, (self.bad_rev_rect.x,
                                          self.bad_rev_rect.y), self.bad_rev_rect)
        bad_rev_surf = self.display_font.render(
            str(self.bad_reviews), True, WHITE)
        self.bad_rev_rect = bad_rev_surf.get_rect()
        self.bad_rev_rect.x = WINDOW_WIDTH - 150
        self.bad_rev_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(bad_rev_surf, self.bad_rev_rect)

# Display time remaining on the screen

    def draw_timer(self, game_window):
        if bool(self.timer_rect):
            game_window.blit(BACKGROUND, (self.timer_rect.x,
                                          self.timer_rect.y), self.timer_rect)
        timer_surf = self.display_font.render(str(
            (WIN_TIME - self.loop_count) // FRAME_RATE), True, WHITE)
        self.timer_rect = timer_surf.get_rect()
        self.timer_rect.x = WINDOW_WIDTH - 250
        self.timer_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(timer_surf, self.timer_rect)

    # Increment the loop_counter & call the other Counters

    def update(self, game_window):
        self.loop_count += 1
        self.increment_bucks()
        self.draw_bucks(game_window)
        self.draw_bad_reviews(game_window)
        self.draw_timer(game_window)

# Create a trap object


class Trap(object):
    # Set up instances of each kind of trap
    def __init__(self, trap_kind, cost, trap_img):
        self.trap_kind = trap_kind
        self.cost = cost
        self.trap_img = trap_img

# Create an object that activates traps


class TrapApplicator(object):
    # Set up TrapApplicator instances
    def __init__(self):
        self.selected = None

    # Activate a trap button
    def select_trap(self, trap):
        if trap.cost <= counters.pizza_bucks:
            self.selected = trap

    def select_tile(self, tile, counters):
        self.selected = tile.set_trap(self.selected, counters)

# Create a background tile object


class BackgroundTile(sprite.Sprite):
    # Set up instances of background tiles
    def __init__(self, rect):
        self.trap = None
        self.rect = rect

# Create a subclass for tiles in the play area


class PlayTile(BackgroundTile):
    # Lay traps on tiles in the play area
    def set_trap(self, trap, counters):
        if bool(trap) and not bool(self.trap):
            counters.pizza_bucks -= trap_cost
            self.trap = trap
            if trap == EARN:
                counters.buck_booster += 1
            return None
    # Do not display anything

    def draw_traps(self, game_window, trap_applicator):
        if bool(self.trap):
            game_window.blit(self.trap.trap_img, (self.rect.x, self.rect.y))

    # Create a sublass for tiles that are trap buttons


class ButtonTile(BackgroundTile):
    # Click on a trap button to select the trap
    def set_trap(self, trap, counters):
        if counters.pizza_bucks >= self.trap.cost:
            return self.trap
        else:
            return None
    # Highlight the trap button that was clicked

    def draw_trap(self, game_window, trap_appplicator):
        if bool(trap_applicator.selected):
            if trap_applicator.selected == self.trap:
                draw.rect(game_window, (238, 190, 47),
                          (self.rect.x, self.rect.y, WIDTH, HEIGHT), 5)

# Create a subclass for tiles that are not interactive


class InactiveTile(BackgroundTile):
    # Do nothing if clicked
    def set_trap(self, trap, counters):
        return None

    # Do not display anything
    def draw_trap(self, game_window, trap_applicator):
        pass


# -------------------------------------------------------
# Create class instances and groups
all_vampires = sprite.Group()

# Create an instance of Counters
counters = Counters(STARTING_BUCKS, BUCK_RATE,
                    STARTING_BUCK_BOOSTER, WIN_TIME)

# Create instances of each kind of trap
SLOW = Trap('SLOW', 5, GARLIC)
DAMAGE = Trap('DAMAGE', 3, CUTTER)
EARN = Trap('EARN', 7, PEPPERONI)

# Create an instance of the TrapApplicator
trap_appplicator = TrapApplicator()
# -------------------------------------------------------
# Background grid
tile_grid = []
tile_color = WHITE
for row in range(6):
    row_of_tiles = []
    tile_grid.append(row_of_tiles)
    for column in range(11):
        tile_rect = Rect(WIDTH * column, HEIGHT * row,
                         WIDTH, HEIGHT)

        if column <= 1:
            new_tile = InactiveTile(tile_rect)
        else:
            if row == 5:
                if 2 <= column <= 4:
                    new_tile = ButtonTile(tile_rect)
                    new_tile.trap = [SLOW, DAMAGE, EARN][column - 2]
                else:
                    new_tile = InactiveTile(tile_rect)
            else:
                new_tile = PlayTile(tile_rect)
        row_of_tiles.append(new_tile)
        if row == 5 and 2 <= column <= 4:
            BACKGROUND.blit(new_tile.trap.trap_img,
                            (new_tile.rect.x, new_tile.rect.y))
        if column != 0 and row != 5:
            if column != 1:
                draw.rect(BACKGROUND, tile_color,
                          (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)


# Display the background image to screen
GAME_WINDOW.blit(BACKGROUND, (0,0))
# -------------------------------------------------------
# Start main game loop

# Game loop
game_running = True
program_running = True

while game_running:

    # -------------------------------------------------------
    # Check for events

    # Checking for and handling events
    for event in pygame.event.get():

        # Exit Loop on quit
        if event.type == QUIT:
            game_running = False
            program_running = False
        # Set up the background tiles to respond to mouse clicks
        elif event.type == MOUSEBUTTONDOWN:
            coordinates = mouse.get_pos()
            x = coordinates[0]
            y = coordinates[1]
            tile_y = y // 100
            tile_x = x // 100
            trap_appplicator.select_tile(
                tile_grid[tile_y][tile_x], counters)

    # Spawn vampire pizza sprites
    if randint(1, SPAWN_RATE) == 1:
        VampireSprite()
# -------------------------------------------------------
# Set up collision detection
# Draw the background grip
for tile_row in tile_grid:
    for tile in tile_row:
        if bool(tile.trap):
            GAME_WINDOW.blit(BACKGROUND, (tile.rect.x,
                                          tile.rect.y), tile.rect)

# Set up detection for collision with background tiles

for vampire in all_vampires:
    tile_row = tile_grid[vampire.rect.y // 100]
    vamp_left_side = vampire.rect.x // 100
    vamp_right_side = (vampire.rect.x +
                       vampire.rect.width) // 100

    if 0 <= vamp_left_side <= 10:
        left_tile = tile_row[vamp_left_side]
    else:
        left_tile = None
    if 0 <= vamp_right_side <= 10:
        right_tile = tile_row[vamp_right_side]
    else:
        right_tile = None

    if bool(left_tile):
        vampire.attack(left_tile)
    if bool(right_tile):
        vampire.attack(right_tile)

# --------------------------------------
# Set win/lose conditions

# Test for lose condition
if counters.bad_reviews >= MAX_BAD_REVIEWS:
    game_running = False

# Test for lose condition
if counters.loop_count > WIN_TIME:
    game_running = False

# -----------------------------------------
# Update displays

# Update enemies
for vampire in all_vampires:
    vampire.update(GAME_WINDOW, counters)

# Update traps that have been set
for tile_row in tile_grid:
    for tile in tile_row:
        tile.draw_trap(GAME_WINDOW, trap_appplicator)

# Update counters
counters.update(GAME_WINDOW)

# Update all images on the screen

display.update()

# Set the time frame
clock.tick(FRAME_RATE)

# -------------------------------------------------------
# Close main game loop

# Set up end game messages
end_font = font.Font(
    'C:\\Users\\hyamy\\Derek_loves_pizza_directory\\D-s-Pizza-\\DPImages\\pizza_font.ttf', 50)
if program_running:
    if counters.bad_reviews >= MAX_BAD_REVIEWS:
        end_surf = end_font.render('GAME OVER', True, WHITE)
    else:
        end_surf = end_font.render('YOU WIN!', True, WHITE)
    GAME_WINDOW.blit(end_surf, (350, 200))
    display.update()

# Enable exit from end game message screen
while program_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            program_running = False
    clock.tick(FRAME_RATE)

# ---------------------------------------------------
# Close end game message loop

# Clean up game

pygame.quit()
