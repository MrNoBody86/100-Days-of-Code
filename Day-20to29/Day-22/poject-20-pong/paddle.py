from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self,starting_pos):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(starting_pos)
        self.shape("square")
        self.seth(UP)
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color("white")


    def move_up(self):
        self.seth(UP)
        self.fd(MOVE_DISTANCE)

    def move_down(self):
        self.seth(DOWN)
        self.fd(MOVE_DISTANCE)

    