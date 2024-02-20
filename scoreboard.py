FONT = ("Courier", 15, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 1
        self.color("black")
        self.goto(-180, 250)
        self.write(f"Current level: {self.current_level}", align="center", font=FONT)

    def update_score(self):
        self.write(f"Current level: {self.current_level}", align="center", font=FONT)

