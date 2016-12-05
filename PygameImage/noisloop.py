import pygame
pygame.init()

clock = pygame.time.Clock()
windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)

crash = pygame.mixer.Sound('crash.wav')
hit = pygame.mixer.Sound('hit.wav')

# count = 0
# while count < 200:
#     if count %4 ==0:
#         crash.play()
#     else:
#         hit.play()
#     count += 1
#     clock.tick(2)
done = False
while not done:
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        hit.play()
    if keys[pygame.K_s]:
        crash.play()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
pygame.quit()
            