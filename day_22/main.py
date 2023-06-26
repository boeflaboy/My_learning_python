from turtle import Screen
from ping_pong_components import RightPaddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping Pong Game in Python')

right_paddle = RightPaddle()

screen.exitonclick()