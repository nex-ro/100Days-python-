import turtle
import  random
from turtle import Turtle,Screen
Turtle=Turtle()
Turtle.shape("turtle")
turtle.width(15)
color=['red','aqua','gray','salmon','purple','blue',"yellow","black","white"]
direction=[0,90,180,270,360]
for i in range(100):
    warna = random.randint(0, len(color)-1)
    turtle.color(30,20,40)
    turtle.left(random.choice(direction))
    turtle.forward(20)


Screen=Screen()
Screen.exitonclick()
