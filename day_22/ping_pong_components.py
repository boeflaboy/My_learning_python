from turtle import Turtle




class RightPaddle:
    def __init__(self):
        self.part = Turtle(shape='square')
        self.part.shapesize(stretch_wid=5, stretch_len=1)
        self.part.penup()
        self.part.color('white')
        self.part.goto(350,0)


    def move_up(self):
        new_y = self.part.ycor() + 20
        self.part.goto(self.part.xcor(), new_y)

    def move_down(self):
        new_y = self.part.ycor() - 20
        self.part.goto(self.part.xcor(), new_y)







