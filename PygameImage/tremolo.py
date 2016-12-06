'''
Created on 2016.12.5

@author: yguo
'''
import math 
import pygame
pygame.init()

pygame.mixer.music.load('LoginScreenIntro.mp3')
pygame.mixer.music.play()

count = 0
while pygame.mixer.music.get_busy():
    volume = abs(math.sin(count))
    pygame.mixer.music.set_volume(volume)
    count += 0.2
    pygame.time.delay(200)