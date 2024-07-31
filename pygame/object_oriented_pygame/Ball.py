import pygame
from pygame.locals import *
import random

# Ball Class
class Ball():
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        
        self.image = pygame.image.load('/Users/macbookpro/Desktop/AI SIBERIA/oop again/pygame/pygame_demo_1_one_image/images/images.jpeg')
        ball_rect = self.image.get_rect()
        self.width = ball_rect.width
        self.height = ball_rect.height
        self.max_width = window_width - self.width
        self.max_height = window_height - self.height
        
        
        # Pick a random starting position
        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)
        
        
        # choose a random speed from a list
        speed_list = [-1,-2,-3,-4,4,3,2,1]
        self.x_speed = random.choice(speed_list)
        self.y_speed = random.choice(speed_list)
        
    def update(self):
        # check if the ball is hitting the walls
        if (self.x < 0) | (self.x >= self.window_width):
            self.x_speed = -self.x_speed
            
        if (self.y < 0) | (self.y >= 0):
            self.y_speed = -self.y_speed
            
        # update the ball's x and y, using the speed in two directions
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))