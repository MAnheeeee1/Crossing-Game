COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle
class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_increment = MOVE_INCREMENT
        self.Starting_move_distace = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.car_list.append(new_car)

    def move_car(self):
        for cars in self.car_list:
            cars.backward(self.Starting_move_distace)













