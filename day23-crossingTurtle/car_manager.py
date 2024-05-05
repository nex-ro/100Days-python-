import random
from turtle import Turtle
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
        self.shape("square")
        self.color(self.COLORS[random.randint(0,len(self.COLORS)-1)])
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.goto(y=random.randint(-230,230),x=280)
        self.yNow=0
        self.xNow=0
    def move(self):
        self.xNow=self.xcor()-self.STARTING_MOVE_DISTANCE
        self.yNow = self.ycor()
        self.goto(x=self.xNow,y=self.yNow)
    def levelUp(self):
        self.STARTING_MOVE_DISTANCE+=self.MOVE_INCREMENT

