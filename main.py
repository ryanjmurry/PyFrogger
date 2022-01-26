import time
from turtle import Screen
from constants import SCREEN_W, SCREEN_H
from frog import Frog
from car_shop import CarShop

screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_W, height=SCREEN_H)

froggy = Frog()
car_shop = CarShop(level=0)

screen.listen()
screen.onkey(froggy.move, "Up")

game_in_progress = True
game_loops = 0

while game_in_progress:
    if game_loops % 6 == 0:
        car_shop.new_car()

    car_shop.move_cars()

    time.sleep(0.1)
    screen.update()
    game_loops += 1

screen.exitonclick()
