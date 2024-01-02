from turtle import Turtle,Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
userbet = screen.textinput(title="Make a bet.",prompt="Which turtle will win the race? Choose a color:")
colors = ["red","yellow","orange","green","blue","purple"]
turtle_list = []


y = -125
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y)
    y += 50
    turtle_list.append(new_turtle)


if userbet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() >= 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == userbet :
                print(f"You've won! The {winning_color} turle is the winner!")
                break
            else :
                print(f"You've lost! The {winning_color} turle is the winner!")
                break
        turtle.fd(random.randint(0,10))

screen.exitonclick()