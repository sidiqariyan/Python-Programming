from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.leftScore = 0
        self.rightScore = 0
        self.hideturtle()
        self.update()
    
    def update(self):
        self.clear()
        self.goto(120, 210)
        self.write(f"Player 2: {self.leftScore}", align="center", font=("Ariel", 20, "bold"))
        self.goto(-120, 210)
        self.write(f"Player 1: {self.rightScore}", align="center", font=("Ariel", 20, "bold"))   
         
    
    def lscore(self):
        self.leftScore += 1
        self.update()
    
    def rscore(self):
        self.rightScore += 1
        self.update()
