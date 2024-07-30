# pygame demo 2 - ball image moves when clicked

# step 1 - import packages
import pygame
from pygame.locals import *
import sys
import random


# step 2 - Define constants
BACKGROUND_BLACK = (0,0,0)
WINDOW_WIDTH = 800
WINDOW_HEIGTH  = 600
FRAMES_PER_SECOND = 30
BALL_HEIGHT_WIDTH = 30
MAX_WIDTH = WINDOW_WIDTH - BALL_HEIGHT_WIDTH
MAX_HEIGHT = WINDOW_HEIGTH - BALL_HEIGHT_WIDTH

# step 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pygame.time.Clock()

# step 4 - load assests: images, sounds, etc
ball_image = pygame.image.load('images/images.jpeg')

# step 5 - initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
ball_Rect = pygame.Rect(ball_x, ball_y, BALL_HEIGHT_WIDTH, BALL_HEIGHT_WIDTH)

# step 6 - Loop Forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # if user clicked mouse button
        if event.type == pygame.MOUSEBUTTONUP:
            # mouse_x, mouse_y = event.pos
            
            # check if the click was in the rect of the ball
            # if so, choose a random new location
            if ball_Rect.collidepoint(event.pos):
                ball_x = random.randrange(MAX_WIDTH)
                ball_y = random.randrange(MAX_HEIGHT)
                ball_Rect = pygame.Rect(ball_x, ball_y, BALL_HEIGHT_WIDTH, BALL_HEIGHT_WIDTH)
    
    # 8 - do any "per frame" actions
    
    
    # 9 - Clear the window
    window.fill(BACKGROUND_BLACK)
    
    
    # 10 - Draw all window elements
    # Draw the ball at the randomized location
    window.blit(ball_image, (ball_x, ball_y))
    
    # 11 - update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)