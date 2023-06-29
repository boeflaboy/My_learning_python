import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()


screen.listen()

player = Player()
screen.onkeypress(player.move_turtle_forward, "Up")
screen.onkeypress(player.move_turtle_downward, "Down")
screen.onkeypress(player.move_turtle_left, "Left")
screen.onkeypress(player.move_turtle_right, "Right")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()


