'''
Created on 2016.11.29

@author: yguo
'''
import pygame
import random
pygame.init()
size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
count = 0

red = pygame.Color('#FF8080')
blue = pygame.Color('#8080FF')
white = pygame.Color('#FFFFFF')
black = pygame.Color('#000000')
done = False

while not done:
    screen.fill(black)
    x = random.randrange(20, size[0]-20)
    y = random.randrange(20, size[1]-20)
    pygame.draw.circle(screen, red, [x, y], 20)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(200)
    count += 1
    print(count)
pygame.quit()