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

while game_in_progress:
    car_shop.new_car()

    car_shop.move_cars()

    # detect collision with a car
    for car in car_shop.cars:
        if car.distance(froggy) < 20:
            game_in_progress = False

    # detect finish
    if froggy.is_at_finish():
        froggy.go_to_start()
        car_shop.level += 1

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
