from turtle import Turtle, Screen, colormode
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


circle1 = Turtle()
colormode(255)
circle1.speed(0)


def draw_spirograph(size):
    for i in range(int(360/size)):
        circle1.color(random_color())
        circle1.circle(radius=100)
        circle1.setheading(circle1.heading() + size)


draw_spirograph(10)
screen = Screen()
screen.exitonclick()
