import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player=Player()
screen.listen()
screen.onkey(player.go_up,"Up")

carmanager= CarManager()
score_board=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move_car()


    #detect collision with car
    for car in carmanager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            score_board.gameover()

    #detect the successful crossing
    if player.is_at_finishline():
        player.go_to_start()
        carmanager.levelup()
        score_board.increase_level()





screen.exitonclick()