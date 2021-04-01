from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self,level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update(level)

    def update(self,level):
        self.clear()
        self.write(f"Level: {level}", font=FONT)


