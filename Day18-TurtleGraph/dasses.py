from turtle import Turtle,Screen
Turtle=Turtle()
Turtle.shape('turtle')

for i in range(20):
    Turtle.penup()
    Turtle.forward(5)
    Turtle.pendown()
    Turtle.forward(5)


Screen=Screen()
Screen.exitonclick()