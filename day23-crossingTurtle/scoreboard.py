from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.FONT = ("Courier", 24, "normal")
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 240)
        self.write(f"Level : {self.level}", align="center", font=self.FONT)


    def gameOver(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GameOver", align="center", font=self.FONT)


    def levelUp(self):
        self.reset()
        self.penup()
        self.goto(-200, 240)
        self.hideturtle()
        self.level=self.level+1
        self.write(f"Level : {self.level}", align="center", font=self.FONT)




