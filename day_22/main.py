import time
from turtle import Screen
from ping_pong_components import Paddle, Ball
from scoreboard import Scoreboard

screen = Screen()

screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping Pong Game in Python')

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")

screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")

ball.setheading(45)
while True:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()


    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    # Right scoreboard
    if ball.xcor() > 445:
        ball.reset_ball_position()
        scoreboard.increate_score_right_player()


    # Left scoreboard
    if ball.xcor() < -445:
        ball.reset_ball_position()
        scoreboard.increate_score_left_player()







screen.exitonclick()



