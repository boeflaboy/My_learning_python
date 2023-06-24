from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
all_turtles = []

turtle_position_vertical = 0
for color in colors:
    turtle_object = Turtle(shape='turtle')
    turtle_object.color(color)
    turtle_object.penup()
    turtle_object.goto(-230, turtle_position_vertical)
    turtle_position_vertical += 25
    all_turtles.append(turtle_object)

user_input = screen.textinput("Bet on a turtle", prompt="What is your bet? ")
if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_input:
                print(f"You win your bet was on the {winning_color}")
            else:
                print(f"You lost. The winner is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
