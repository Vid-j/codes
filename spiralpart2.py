import colorsys
import turtle

t = turtle.Turtle()
t.hideturtle()
turtle.bgcolor('black')
t.speed(0)
t.pensize(2)

n = 36
h = 0
increment = 0.5 / n  # Decrease this value to change the hue more slowly

for i in range(90):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += increment
    t.pencolor(c)
    for j in range(5):
        t.forward(i - 3)
        t.right((9 * 6)-n)
        t.left(8)
    t.right(115)

# Move the turtle back to the start position
t.home()

# Draw the stem
t.pencolor('green')
t.pensize(5)  # Increase the thickness of the stem
t.right(90)
for i in range(10):
    for i in range(5):
        t.forward(5)
        t.right(10)

    for i in range(5):
        t.forward(5)
        t.left(10)
t.penup()
t.goto(-50, -150)
t.pendown()
t.right(105)
for i in range(5):
    t.circle(50, 60)  # Draw a part of a circle
    t.right(120)  # Turn the turtle
    t.circle(50, 60)  # Draw another part of a circle
    t.left(120)

turtle.done()