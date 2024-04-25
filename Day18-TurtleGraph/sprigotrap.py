from turtle import Turtle ,Screen
t=Turtle()
t.color("black")
for i in range(360):
    t.circle(100)
    t.setheading(i*5)

Screen=Screen()
Screen.exitonclick()