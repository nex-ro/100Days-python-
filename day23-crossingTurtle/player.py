from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.STARTING_POSITION = (0, -280)
        self.MOVE_DISTANCE = 10
        self.left(90)
        self.FINISH_LINE_Y = 280
        self.shape("turtle")
        self.penup()
        self.goto(self.STARTING_POSITION)

    def moveF(self):
        self.forward(self.MOVE_DISTANCE)







