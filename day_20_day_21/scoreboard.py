from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.highscore = self.read_from_scoreboard_file()




    @staticmethod
    def write_to_scoreboard_file(highscore):
        with open('data.txt', 'w') as scoreboard_file:
            scoreboard_file.write(str(highscore))

    def read_from_scoreboard_file(self):
        with open('data.txt', 'r') as scoreboard_file:
            score = int(scoreboard_file.read())
        return score



    def update_score(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} Highscore: {self.highscore}", align='center', font=('Arial', 15, 'normal'))



    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_to_scoreboard_file(self.score)
        self.score = 0


