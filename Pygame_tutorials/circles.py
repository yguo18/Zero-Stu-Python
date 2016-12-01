import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)

pygame.display.set_caption('Circles')

colour = pygame.Color('#FFFFFF')

done = False
while not done:
    pygame.draw.circle(screen, colour, [200, 150], 50)
    pygame.draw.rect(screen, colour, [10, 20, 30, 40])  # include frame and w h
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()