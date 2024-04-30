from turtle import Turtle
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0,0)
        self.penup()
        self.yDir=10
    def move(self):
        x = self.xcor() +13
        y = self.ycor() +self.yDir
        self.goto((x, y))
    def bounces(self):
        self.yDir*=-1
