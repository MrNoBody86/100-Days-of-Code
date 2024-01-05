import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.cross,"Up")

loop_num = 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 300 :
        player.reset()
        car_manager.speed_increse()
        scoreboard.level += 1
        scoreboard.level_up()
        

    if loop_num == 6:
        car_manager.create_cars()
        loop_num = 0

    car_manager.move_car(car_manager.all_cars)

    for car in car_manager.all_cars :
        if player.distance(car) < 22 :
            game_is_on = False
            scoreboard.game_over()



    loop_num += 1

    


screen.exitonclick()
