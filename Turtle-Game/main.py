from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

newSnake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(newSnake.up, "Up")
screen.onkey(newSnake.down, "Down")
screen.onkey(newSnake.right, "Right")
screen.onkey(newSnake.left, "Left")
# screen.onkey(newSnake.control("Down"))
isGameOn = True

while isGameOn:
    screen.update()
    time.sleep(0.1)

    newSnake.move()

    if newSnake.head.distance(food) < 15:
        food.pos()
        newSnake.extend()
        score.increseScore()
    if newSnake.head.xcor() > 280 or newSnake.head.xcor() < -280 or newSnake.head.ycor() > 280 or newSnake.head.ycor() < -280:
        isGameOn = False
        score.gameOver()

    for segment in newSnake.segments:
        if segment == newSnake.head:
            pass
        elif newSnake.head.distance(segment) < 10:
            isGameOn = False
            score.gameOver()

screen.exitonclick()
