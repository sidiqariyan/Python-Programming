from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000")
screen.title("Pong Game")
screen.tracer(0)

paddleRight = Paddle((350))
paddleLeft = Paddle((-350))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddleRight.upMovement, "Up")
screen.onkey(paddleRight.downMovement, "Down")
screen.onkey(paddleLeft.upMovement, "w")
screen.onkey(paddleLeft.downMovement, "s")

isGameOn = True
while isGameOn:
    timing = time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounceY()

    if ball.distance(paddleRight) < 50 and ball.xcor() > 320 or ball.distance(paddleLeft) < 50 and ball.xcor() < -320:
        ball.bounceX()
    
    if ball.xcor() > 380:
        score.rscore()
        ball.reset()
    
    if ball.xcor() < -380:
        ball.reset()
        score.lscore()
    
    
screen.exitonclick()
