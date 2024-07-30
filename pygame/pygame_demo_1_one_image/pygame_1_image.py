from pathlib import Path
import pygame
from pygame.locals import *
import sys

BASE_PATH = Path(__file__).resolve().parent

# Build a path to the file in the images folder
path_to_ball = BASE_PATH/'images/images.jpeg'

# Define the constant for the Windows
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGT = 480
FRAMES_PER_SECOND = 30

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGT))
clock = pygame.time.Clock()

# load the assests
ball_image = pygame.image.load('images/images.jpeg')

# Initialize variables

# loop forever
while True:
    # check for and handle events
    for event in pygame.event.get():
        # clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    # Do any "per frame" actions
    
    
    # Clear the window
    window.fill(BLACK)
    
    # draw all window elements
    window.blit(ball_image, (100, 200))
    
    # update the window
    pygame.display.update()
    
    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
