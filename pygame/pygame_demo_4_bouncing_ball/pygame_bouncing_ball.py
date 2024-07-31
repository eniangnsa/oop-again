# pygame demo - 4, one image bouncing around the window

# 1 - import the packages
import pygame
from pygame.locals import *
import sys
import random


# 2 - Define Constants
BLACK_BACKGROUND = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGTH = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGTH = 100
N_PIXELS_PER_FRAME = 3


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
caption = pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

# 4 - Load assets: images, sounds, etc
ball_image = pygame.image.load('images/images.jpeg')

# 5 - Initialize variable
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGTH
MAX_HEIGHT = WINDOW_HEIGTH - BALL_WIDTH_HEIGTH
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_PER_FRAME
y_speed = N_PIXELS_PER_FRAME

# 6 - Loop Forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # 8 - Do any "per frame" actions
    if (ball_x < 0) | (ball_x >= MAX_WIDTH):
        x_speed = -x_speed # reverse x direction
        
    if (ball_y < 0) | (ball_y >= MAX_HEIGHT):
        y_speed = -y_speed # reverse y direction
        
    # Update the ball's location, using the speed in two directions
    ball_x = ball_x + x_speed
    ball_y = ball_y + y_speed
    
    # 9 - Clear the window before drawing it again
    window.fill(BLACK_BACKGROUND)
    
    # 10 - Draw the window elements
    window.blit(ball_image, (ball_x, ball_y))
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)


