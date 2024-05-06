import random
from turtle import Turtle

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refres()

    def refres(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.setposition(x, y)
