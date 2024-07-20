import pygame
from pygame.locals import *
import sys

# define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGT = 480
FRAMES_PER_SECOND = 30

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGT))
clock = pygame.time.Clock()

# Load assets: images, sounds etc

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
    
    # update the window
    pygame.display.update()
    
    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
    
    