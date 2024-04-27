from turtle import Turtle, Screen
from snake import snake
import time
screen=Screen()
screen.setup(width=600 ,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake=snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while True :
    time.sleep(0.1)
    screen.update()
    snake.move()




screen.exitonclick()