from turtle import Turtle
from constants import SCREEN_H, SCREEN_W

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
Y_POS = SCREEN_H // 2 - 40
X_POS = -SCREEN_W // 2 + 80
POS = (X_POS, Y_POS)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.level = 1
        self.pu()
        self.goto(POS)

    def broadcast(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

