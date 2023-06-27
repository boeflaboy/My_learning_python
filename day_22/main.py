from turtle import Screen
from ping_pong_components import RightPaddle

screen = Screen()

screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping Pong Game in Python')

paddle = RightPaddle()


screen.listen()

screen.onkeypress(paddle.move_up, "Up")
screen.onkeypress(paddle.move_down, "Down")

while True:
    screen.update()




screen.exitonclick()
