from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier',80,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,False,align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(self.r_score,False,align=ALIGNMENT,font=FONT)

    def l_point(self):
        self.l_score += 1
        self.score_update()

    def r_point(self):
        self.r_score += 1
        self.score_update()