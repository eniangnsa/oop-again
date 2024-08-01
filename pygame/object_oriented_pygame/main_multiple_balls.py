# multiple bouncing balls

import pygame
from pygame.locals import *
from Ball import *
import random
import sys

# 2 - Define constants
BLACK_BACKGROUND = (0,0,0)
WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
N_BALLS = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
caption = pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

# 4 - Load Assests: images, sounds, etc


# 5 - Initialize Variables
ball_list = []
for ball in range(0, N_BALLS):
    # create a ball object and append it to the ball_list
    ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ball_list.append(ball)
    
    
# 6 - Loop Forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Do any "per frame" actions
    for ball in ball_list:
        ball.update()
        
    # 9 - Clear the window
    window.fill(BLACK_BACKGROUND)
    
    # 10 - Draw the elements
    for ball in ball_list:
        ball.draw()
        
    # 11 - update the window
    pygame.display.update()
    
    # 12 - slow things down a bit
    clock.tick(FRAMES_PER_SECOND)