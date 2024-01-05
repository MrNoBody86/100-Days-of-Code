from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars= []
        self.speed =  STARTING_MOVE_DISTANCE


    def create_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(x=280,y=random.randint(-250,250))
        self.all_cars.append(new_car)
    
    def move_car(self,all_cars):
        for car in all_cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x,car.ycor())
    
    def speed_increse(self):
        self.speed += MOVE_INCREMENT
    
        


