from turtle import Turtle,Screen
from paddle import paddle
from ball import ball
import time
screen=Screen()
screen.bgcolor("black")

screen.setup(width=800,height=600)
paddle1 =paddle((-350,0))
paddle2 =paddle((350,0))

screen.listen()
screen.onkey(paddle1.moveUp,"Up")
screen.onkey(paddle1.moveDown,"Down")

screen.onkey(paddle2.moveUp,"w")
screen.onkey(paddle2.moveDown,"s")
ball=ball()
is_Game=True
while is_Game:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if(ball.ycor()>280 or ball.ycor() < -280):
        ball.bounces()




screen.exitonclick()
