'''
Created on 2016.12.5

@author: yguo
'''
import pygame
pygame.init()

# sound = pygame.mixer.Sound('hit.wav')
pygame.mixer.music.load('music.mp3')
# sound.play()
pygame.mixer.music.play()
# pygame.time.wait(int(sound.get_length())*1000)
while pygame.mixer.music.get_busy():
    pygame.time.delay(200)