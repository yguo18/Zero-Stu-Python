'''
Created on 2016.11.29

@author: yguo
'''

import random
import pygame
pygame.init()

width = 400
height = 300
windowSize = [width, height]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

sqrW = width / 10
sqrH = height / 10
done = False
while not done:
    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    
    x = random.randrange(0, width, sqrW)
    y = random.randrange(0, height,sqrH)
    pygame.draw.rect(screen, (red, green, blue), (x, y, sqrW, sqrH))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
pygame.quit()       