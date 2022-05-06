import random
import turtle

turtle.colormode(255)
timmy = turtle.Turtle()
screen = turtle.Screen()
timmy.width(2)
timmy.speed("fast")


def set_point(x, y):
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()


color_list = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "white"]


def draw_circle(radius):
    timmy.fillcolor(color_list[random.randint(0, len(color_list) - 1)])
    timmy.begin_fill()
    timmy.circle(radius)
    timmy.end_fill()


set_point(0, 0)
draw_circle(100)
set_point(0, 12.5)
draw_circle(87.5)
set_point(0, 25)
draw_circle(75)
set_point(0, 50)
draw_circle(50)


screen.exitonclick()
