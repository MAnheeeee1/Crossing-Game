import random
import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
STARTING_POSITION = (0, -300)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player_game = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player_game.move, "w")
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move_car()
    for cars in car_manager.car_list:
        if player_game.distance(cars) < 30:
            game_is_on = False
    if player_game.ycor() > 250:
        player_game.goto(STARTING_POSITION)
        score_board.current_level += 1
        score_board.clear()
        score_board.update_score()
        car_manager.Starting_move_distace += car_manager.move_increment








screen.exitonclick()
