from turtle import Turtle

snake_part_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segments = []
        for position in snake_part_position:
            snake_part = Turtle(shape='square')
            snake_part.color('white')
            snake_part.penup()
            snake_part.goto(position)
            self.segments.append(snake_part)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)



