'''
Created on 2016.11.29

@author: yguo
'''
import pygame
pygame.init()
size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False
while not done:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        print('hello')
    elif keys[pygame.K_a]:
        print('world')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
pygame.quit()