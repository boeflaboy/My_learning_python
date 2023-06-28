from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 190)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))


    def increate_score_left_player(self):
        self.left_score += 1
        self.update_scoreboard()

    def increate_score_right_player(self):
        self.right_score += 1
        self.update_scoreboard()





