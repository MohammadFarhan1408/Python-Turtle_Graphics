from turtle import Turtle, Screen, colormode
import random

turtle1 = Turtle()
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


direction = [0, 45, 90, 135, 180, 225, 270]
turtle1.pensize(10)

for _ in range(200):
    turtle1.color(random_color())
    turtle1.forward(30)
    turtle1.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
