'''
Created on 2016.11.29

@author: yguo
'''

import pygame
pygame.init()

width = 400
height = 300
windowSize = [width, height]
screen = pygame.display.set_mode(windowSize)
red = 64
green = 64
blue = 0
# colour = pygame.Color("#647350")
colour = [red, green, blue]
row = 0
done = False
while not done:
    increment = 255/100
    while row <= height:
        pygame.draw.rect(screen, colour, (0, row, width, row+ increment))
        pygame.display.flip()
        if colour[2] + increment < 255:
            colour[2] += increment
        row += increment
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()