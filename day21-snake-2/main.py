from turtle import Turtle, Screen
from snake import snake
import time
from scoreBoard import scoreBoard
from food import food
# deklarasi

screen=Screen()
screen.setup(width=600 ,height=600)
screen.bgcolor("black")
screen.tracer(0)

Food=food()
snake=snake()
scoreBoard=scoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

isLoop=True
while isLoop :
    time.sleep(0.1)
    screen.update()
    snake.move()

    if(snake.turtles[0].distance(Food)<15):
        snake.extend()
        Food.refres()
        scoreBoard.increment()
        scoreBoard.updateScore()

    if(snake.turtles[0].xcor()>300 or snake.turtles[0].xcor()<-300 or snake.turtles[0].ycor()>300  or snake.turtles[0].ycor()<-300 ):
        scoreBoard.gameOver()
        isLoop=False
        break
    for segment in snake.turtles:
        if(segment== snake.turtles[0]):
            pass
        elif(snake.turtles[0].distance(segment)<10):
            isLoop=False
            scoreBoard.gameOver()
            break



screen.exitonclick()