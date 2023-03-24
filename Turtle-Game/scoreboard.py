from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.updateScore()
        
    def updateScore(self):
        self.write(f'Score: {self.score}', align="center", font=("Ariel", 24, "bold"))
    
    def gameOver(self):
        self.goto(0, 0)
        self.write('Game Over', align="center", font=("Ariel", 24, "bold"))
        
    
    def increseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()
        
