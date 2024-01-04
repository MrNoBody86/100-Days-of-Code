from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game 🏓")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")
screen.onkey(paddle_l.move_up,"w")
screen.onkey(paddle_l.move_down,"s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect colision with wall  
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    
    #Detect colision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()

    #Detect miss with paddle_r
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_point()


    #Detect miss with paddle_l
    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score  == 10 :
        game_is_on = False
    elif scoreboard.r_score == 10 :
        game_is_on = False








screen.exitonclick()