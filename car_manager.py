from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_Y = []
for i in range(-220, 280, 20):
    START_Y.append(i)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.lt(180)
        self.speed = 5

    def start(self):
        self.goto(random.randint(-280, 280), random.choice(START_Y))

    def create(self):
        self.goto(280, random.choice(START_Y))

    def move(self):
        self.fd(self.speed)

    def update_speed(self):
        self.speed += 10
