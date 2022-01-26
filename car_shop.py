from turtle import Turtle
from constants import SCREEN_H, SCREEN_W
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_Y = SCREEN_H // 2 - 50
MIN_Y = -MAX_Y + 50
STARTING_X = SCREEN_W // 2


class CarShop:
    def __init__(self, level):
        self.cars = []
        self.level = level

    def new_car(self):
        rand = randint(1, 6)
        if rand == 6:
            new_car = Turtle(shape="square")
            new_car.right(180)
            new_car.color(choice(COLORS))
            new_car.pu()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            rand_y = randint(MIN_Y, MAX_Y)
            new_car.goto(STARTING_X, rand_y)
            self.cars.append(new_car)

    def move_cars(self):
        move_distance = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.level)
        for car in self.cars:
            car.forward(move_distance)
