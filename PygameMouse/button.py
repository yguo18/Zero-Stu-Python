'''
Created on 2016.12.4

@author: yguo

failed
'''
import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

black = pygame.Color("#000000")
white = pygame.Color("#FFFFFF")
btnColour = pygame.Color("#A45C8F")

btnWidth = 50
btnLength = 20
btnX = (windowSize[0] - btnWidth) / 2
btnY = (windowSize[1] - btnLength) / 2

toggled = False
pos = (0, 0)

done = False
while not done:
    if toggled:
        screen.fill(black)
    else:
        screen.fill(white)
    
    pygame.draw.rect(screen, btnColour, [btnX, btnY, btnWidth, btnLength])
    if btnX <= pos[0] <= btnX + btnWidth and btnY <= pos[1] <= btnY + btnLength:
        toggled = not toggled
        pos = [0, 0]
        
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            done = True
            
pygame.quit()
