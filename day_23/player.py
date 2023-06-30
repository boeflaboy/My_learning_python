from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
SWITCH_LANE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.current_position = self.xcor()

    def move_turtle_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_turtle_downward(self):
        self.forward(-MOVE_DISTANCE)

    def move_turtle_left(self):
        self.current_position -= SWITCH_LANE
        self.goto(self.current_position, self.ycor())


    def move_turtle_right(self):
        self.current_position += SWITCH_LANE
        self.goto(self.current_position, self.ycor())


    def reset_player_position(self):
        self.goto(STARTING_POSITION)
