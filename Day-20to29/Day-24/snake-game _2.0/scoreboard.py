from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier',20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0,y=270)
        self.score_update()

    
    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",False,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("Game Over",False,align=ALIGNMENT,font=FONT)