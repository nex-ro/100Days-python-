import random
from turtle import Turtle


class paddle(Turtle):
    def __init__(self,location):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(location)
    def moveUp(self):
        x= self.xcor()
        y=self.ycor()+20
        if (y >260):
            pass
        else:
            self.goto((x, y))

    def moveDown(self):
        x = self.xcor()
        y = self.ycor() -20
        if(y<-260):
            pass
        else:
            self.goto((x, y))
