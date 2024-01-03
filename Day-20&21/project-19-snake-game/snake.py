from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head  = self.snake_segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    
    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].pos())


    def move(self):
        for seg_num in range(len(self.snake_segments)-1,0,-1):
            new_corr = self.snake_segments[seg_num - 1].pos()
            self.snake_segments[seg_num].goto(new_corr)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)