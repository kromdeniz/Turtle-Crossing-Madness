import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_num = 25
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Krom Abi's Turtle Crossing Madness")

def game_over():
    msg = Turtle()
    msg.penup()
    msg.hideturtle()
    msg.write("Game Over", font=("ariel", 20, "bold"), align="center")


level = 1
scoreboard = Scoreboard(level)
player = Player()
screen.onkey(player.move, "Up")
cars = []

while len(cars) < car_num:
    x = CarManager()
    x.start()
    cars.append(x)

game_is_on = True
while game_is_on:
    if player.ycor() == 280:
        level += 1
        scoreboard.update(level)
        for ch in cars:
            ch.update_speed()
        player.goto(0, -280)

    if len(cars) >= car_num:
        for i in cars:
            if i.xcor() < -275:
                current_speed = i.speed
                cars.remove(i)
                i.hideturtle()
            i.move()
            if i.distance(player) < 30:
                game_over()
                game_is_on = False
    else:
        new_car = CarManager()
        new_car.create()
        new_car.speed = current_speed
        cars.append(new_car)

    screen.listen()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
