import random
import turtle
from turtle import Turtle
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 280)

    def write_score(self):
        turtle.write("Score is: ", align='center',)