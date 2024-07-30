# pygame demo 3(a) - one image, move by the keyboard
# so the goal of this game is to move the ball to the target 

# import the packages
import pygame
from pygame.locals import *
import sys
import random


# Define Constants
BACKGROUND_BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGTH = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGTH = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGTH
MAX_HEIGHT = WINDOW_HEIGTH - BALL_WIDTH_HEIGTH
TARGET_X = 50
TARGET_Y = 20
TARGET_WIDTH_HEIGTH = 10
N_PIXELS_TO_MOVE = 3


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pygame.time.Clock()


# 4 - Load the assests
ball_image = pygame.image.load('images/images.jpeg')
target_image = pygame.image.load('images/edwin-andrade-4V1dC_eoCwg-unsplash.jpg')

# 5 - Initialize the position of the variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
target_Rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGTH, TARGET_WIDTH_HEIGTH)

# 6 - Loop Forever
while True:
    
    # 7 - Event handlers
    for event in pygame.event.get():
        # to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Check if user pressed a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_x = ball_x - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ball_x = ball_x + N_PIXELS_TO_MOVE
            
            elif event.key == pygame.K_UP:
                ball_y = ball_y - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ball_y += N_PIXELS_TO_MOVE
                
    
    # 8 - Do any "per frame" action
    
    # Create the ball object
    ball_Rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGTH, BALL_WIDTH_HEIGTH)
    
    # Check if the ball is colliding with the target
    if ball_Rect.colliderect(target_Rect):
        print("Ball is touching the target")
        
    # 9 - Clear Window
    window.fill(BACKGROUND_BLACK)
    
    # 10 - Draw all window elements
    window.blit(target_image, (TARGET_X, TARGET_Y))
    window.blit(ball_image, (ball_x, ball_y))
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)