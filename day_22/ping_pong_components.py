from turtle import Turtle

RIGHT_PADDLE_POSTION_X = 350
RIGHT_PADDLE_POSTION_Y = 0




class RightPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=20)
        self.goto(RIGHT_PADDLE_POSTION_X, RIGHT_PADDLE_POSTION_Y)
        self.color('white')
