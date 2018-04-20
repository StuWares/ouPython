# draw a tree using two loops
from turtle import *

number_of_triangles = 3
length = 40
distance_to_move = 35

for triangle in range(number_of_triangles):

    # first triangle
    for sides in range(3):
        forward(length)
        left(120)

    # move to new position
    penup()
    left(90)
    forward(distance_to_move)
    right(90)
    forward(5)
    pendown()

    length = length - 10
    distance_to_move = distance_to_move - 10
    number_of_triangles = number_of_triangles - 1
