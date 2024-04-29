from turtle import Turtle

class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score :{self.score}",align="center", font=('Arial', 24, 'normal'))

    def increment(self):
        self.score = self.score + 1

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GameOVer", align="center", font=('Arial', 24, 'normal'))



