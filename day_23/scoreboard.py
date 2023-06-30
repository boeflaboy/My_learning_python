from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.score = 0
        self.print_score()


    def update_score_board(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}", align="center", font=('Arial', 16, 'normal'))







