from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def cross(self):
        self.fd(MOVE_DISTANCE)
    
    def reset(self):
        self.goto(STARTING_POSITION)
