# Draw 3 equilateral triangles at the points of an undrawn right angle triangle

from turtle import *

# draw a triangle
for sides in range(1, 4):
    forward(40)
    left(120)

# first move
penup()
forward(100)
pendown()

# draw a triangle
for sides in range(1, 4):
    forward(40)
    left(120)

# final move
penup()
left(180)
forward(100)
right(90)
forward(100)
right(90)
pendown()

# draw a triangle
for sides in range(1, 4):
    forward(40)
    left(120)
