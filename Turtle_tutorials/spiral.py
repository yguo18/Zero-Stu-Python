import turtle
length = 10
angle = 90
# for i in range(100):
#     turtle.forward(length)
#     turtle.left(angle)
#     length = length + 10
while length<100:
    turtle.forward(length)
    turtle.right(angle)
    length = length + 10
    
turtle.done()