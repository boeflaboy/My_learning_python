from turtle import Screen
from ping_pong_components import Paddle, Ball

screen = Screen()

screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping Pong Game in Python')

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()

screen.listen()

screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")

screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")

ball.setheading(45)
while True:
    screen.update()
    ball.move_ball()

    if ball.xcor() > 288 or ball.xcor() < -288:
        ball.setheading(-45)




screen.exitonclick()
