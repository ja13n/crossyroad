import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
car_manager.hideturtle()
scoreboard = Scoreboard()

screen.onkey(player.go_forward, "W".lower())
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.car_speed()
    screen.update()
    car_manager.generate_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == 300:
        player.goto(0, -280)
        car_manager.car_speed()
        scoreboard.update_scoreboard()


screen.exitonclick()
