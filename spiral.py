# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import colorsys
import turtle
colors = ['pink', 'purple', 'blue']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%3])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)