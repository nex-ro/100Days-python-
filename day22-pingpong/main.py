from turtle import Turtle,Screen
from paddle import paddle
from ball import ball
from gui import gui
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
gui=gui()
while is_Game:
    screen.update()
    time.sleep(0.1)
    screen.update()
    ball.move()

    # check if touch wall
    if(ball.ycor()>280 or ball.ycor() < -280):
        ball.bounces()
    #     check it touch rightPaddle
    if(paddle2.distance(ball) < 50 and ball.xcor() > 330):
        ball.touchPaddle()
    #     check it touch leftPaddle
    if(paddle1.distance(ball) < 50 and ball.xcor() < -330):
        ball.touchPaddle()

    if(ball.xcor()>380):
        gui.upScore2()
        ball.restart()
    if(ball.xcor() <-380):
        gui.upScore1()
        ball.restart()




screen.exitonclick()
