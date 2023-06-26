from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score = 0



    def update_score(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}", align='center', font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=('Courier', 24, 'normal'))
