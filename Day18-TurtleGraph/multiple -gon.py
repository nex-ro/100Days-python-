import turtle
import  random
from turtle import Turtle,Screen
Turtle=Turtle()
Turtle.shape("classic")

color=['red','aqua','gray','salmon','purple','blue',"yellow","black","white"]

for i in range(3,8):
    for j in range(i):
        Turtle.color(color[i])
        Turtle.forward(100)
        Turtle.right((360/i))

Screen=Screen()
Screen.exitonclick()
