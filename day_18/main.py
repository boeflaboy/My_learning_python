import colorgram
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.speed('fastest')
extracted_colors = []
screen.colormode(255)
colors = colorgram.extract('image.jpg', 8)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    extracted_colors.append((r, g, b))


def dotted_line():
    for i in range(25):
        tim.dot(10, random.choice(extracted_colors))
        tim.penup()
        tim.forward(25)
        tim.pendown()


y_point = 30
for i in range(20):
    dotted_line()
    tim.penup()
    tim.goto(0, y_point)
    y_point += 30

screen.exitonclick()
