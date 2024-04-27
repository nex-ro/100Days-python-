from turtle import Turtle
class snake:
    def __init__(self):
        self.turtles = []
        for i in range(3):
            t = Turtle()
            t.shape("square")
            t.goto(x=i * -20, y=0)
            t.color("white")
            t.penup()
            self.turtles.append(t)
    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            xCor = self.turtles[i - 1].xcor()
            yCor = self.turtles[i - 1].ycor()
            self.turtles[i].goto(xCor, yCor)
        self.turtles[0].forward(20)
    def up(self):
        if self.turtles[0].heading()!= 270:
            self.turtles[0].setheading(90)
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)
    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)
    def right(self):
        if self.turtles[0].heading() !=180:
            self.turtles[0].setheading(0)