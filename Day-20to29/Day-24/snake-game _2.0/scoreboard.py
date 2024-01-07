from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier',20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day-20to29\Day-24\snake-game _2.0\data.txt") as data_file : # Relative path
            self.highscore = eval(data_file.read())
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
            with open("Day-20to29\Day-24\snake-game _2.0\data.txt",mode="w") as data_file :
                data_file.write(str(self.highscore))
            
        self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("Game Over",False,align=ALIGNMENT,font=FONT)