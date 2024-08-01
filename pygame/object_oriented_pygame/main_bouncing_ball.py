# using the Ball Class

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *

# 2 - Define constants
BLACK_BACKGROUND = (0,0,0)
WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
caption = pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

# 4 - Load assets: images, sounds, etc


# 5 - Initialize Variable
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# 6 - Loop Forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # 8 - Do any "per frame" actions
    ball.update() # tell the ball to update itself
    
    # 9 - Clear the window before drawing it again
    window.fill(BLACK_BACKGROUND)
    
    # 10 - Draw the window elements
    ball.draw() # tell the ball to draw itself
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
    
    
    