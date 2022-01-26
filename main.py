import time
from turtle import Screen
from constants import SCREEN_W, SCREEN_H
from frog import Frog

screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_W, height=SCREEN_H)

froggy = Frog()

screen.listen()
screen.onkey(froggy.move, "Up")

game_in_progress = True

while game_in_progress:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
