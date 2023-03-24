from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#eee")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position, 0)


    def upMovement(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def downMovement(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
