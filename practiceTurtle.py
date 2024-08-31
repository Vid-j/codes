from turtle import *
from random import random

t = Turtle()
t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("pink")
hideturtle()# hide the turtle
for i in range(20):
    i+=100
    circle(random()*i)
    circle(-random()*i)
    circle(random()*(-i))
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

t.screen.mainloop()
