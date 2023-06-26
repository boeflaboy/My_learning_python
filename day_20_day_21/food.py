from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')

    def new_location(self):
            x_place = random.randint(-280, 280)
            y_place = random.randint(-280, 280)
            self.goto(x_place, y_place)

