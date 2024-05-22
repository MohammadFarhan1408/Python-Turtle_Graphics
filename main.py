from turtle import *

turtle1 = Turtle()


def draw_shape(num_slides):
    angle = 360 / num_slides
    for _ in range(num_slides):
        turtle1.forward(50)
        turtle1.right(angle)


for i in range(3, 10):
    draw_shape(i)

screen = Screen()
screen.exitonclick()
