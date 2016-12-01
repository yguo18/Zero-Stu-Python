'''
Created on 2016.11.29

@author: yguo
'''
import pygame
import random
import math
from Crypto.Random.random import randrange
from bokeh.colors import white
pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = int(size[0] / 2)
y = int(size[1] / 2)
ballX = random.randrange(20, size[0]-20)
ballY = random.randrange(20, size[1]-20)
goalX = size[0]/2-10
goalY = size[1]/2-10
goalW = 50
goalH = 40
point = 0

red = pygame.Color('#FF8080')
blue = pygame.Color('#8080FF')
white = pygame.Color('#FFFFFF')
black = pygame.Color('#000000')
count = 0
done = False
def checkOffScreenX(x):
    ''' check x axis whether in screen edge'''
    if x > size[0]-20:
        x = size[0]-20
    if x < 20:
        x = 20
    return x
def checkOffScreenY(y):
    ''' check y axis whether in screen edge'''
    if y > size[1]-20:
        y = size[1]-20
    if y < 20:
        y = 20
    return y
# def checkTouching():
#     global x
#     global ballX
#     global y
#     global ballY
#     
#     if -10 < y - ballY < 10 and -10 < x - ballX < 10:
#         pygame.draw.circle(screen, white, [x, y], 40)
#         xDiff = x - ballX
#         yDiff = y - ballY
#         if ballX == 0:
#             xDiff -= 5
#         elif ballX == size[0]:
#             xDiff += 5
#         if ballY == 0:
#             yDiff -= 5
#         elif ballY == size[1]:
#             yDiff += 5
#         x += xDiff * 3
#         ballX -= xDiff * 3
#         y += yDiff * 3
#         ballY -= yDiff * 3
def touchEdge():
    ''' check two circle whether touch and ball circle whether touch windows corner'''
    global x
    global ballX
    global y
    global ballY
    distance = math.pow((x-ballX),2)+math.pow((y-ballY), 2)
    if distance <= 400:
        # draw a big
        pygame.draw.circle(screen, white, [x, y], 40)
        xDiff = x - ballX
        yDiff = y - ballY
        if xDiff == 0:
            if yDiff < 0:
                yDiff += 1
            else:
                yDiff -= 1 
        else:
            alpha = math.atan2(yDiff, xDiff)
            xDiff += math.cos(alpha) * 2
            yDiff += math.sin(alpha) * 2
    
#         x += int(xDiff * 2)
        ballX -= int(xDiff * 2)
#         y += int(yDiff * 2)
        ballY -= int(yDiff * 2)
    if (ballX==20 and (ballY==20 or ballY ==(size[1]-20))) or (ballX==size[0]-20 and (ballY == 20 or ballY ==size[1]-20)):
        ballX = random.randrange(20,size[0]-20)
        ballY = random.randrange(20,size[1]-20)
timeStart = pygame.time.get_ticks()
while not done:
    screen.fill(black)
    # draw the goal
    pygame.draw.rect(screen,white, (goalX, goalY, goalW, goalH))
    if goalX <= ballX <= goalX + goalH and goalY <= ballY <= goalY + goalH:
        point += 1
        ballX = random.randrange(20,size[0]-20)
        ballY = random.randrange(20,size[1]-20)
    keys = pygame.key.get_pressed()
    #move
    if keys[pygame.K_w]:
        y -= 1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1
    # draw Circle
    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    ballX = checkOffScreenX(ballX)
    ballY = checkOffScreenY(ballY)
    m = [x, y]
    touchEdge()
    
#     x = checkOffScreenX(x)
#     y = checkOffScreenY(y)
#     ballX = checkOffScreenX(ballX)
#     ballY = checkOffScreenY(ballY)
    pygame.draw.circle(screen, red, m, 20)
    pygame.draw.circle(screen, blue, [ballX, ballY], 20)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(72)
    timeNow = pygame.time.get_ticks()
    if timeNow-timeStart >= 6000:
        done = True
    count += 1
    print(count)
pygame.quit()
print("total points: " + str(point))