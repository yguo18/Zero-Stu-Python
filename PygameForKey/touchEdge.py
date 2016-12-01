'''
Created on 2016.11.29

@author: yguo
'''
# import math
# 
# radious = 400
# def distanCenters(x, y, ballX, ballY):
#     return math.pow((x-ballX),(y-ballY))
# def touchEdge(x, y, ballX, ballY):
#     distance = distanCenters(x, y, ballX, ballY)
#     if distance <= radious:
#         # draw a big
#         xDiff = x - ballX
#         yDiff = y - ballY
#         if xDiff == 0:
#             if yDiff < 0:
#                 yDiff += 5
#             else:
#                 yDiff -=5 
#         else:
#             alpha = math.atan2(yDiff, xDiff)
#             xDiff += math.cos(alpha) * 10
#             yDiff += math.sin(alpha) * 10
#     
#         x += xDiff * 2
#         ballX -= xDiff * 2
#         y += yDiff * 2
#         ballY -= yDiff * 2
#     