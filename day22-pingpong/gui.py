from turtle import Turtle
class gui(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.score2=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"{self.score}     :     {self.score2}", align="center", font=('Arial', 24, 'normal'))

    def upScore1(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}     :     {self.score2}", align="center", font=('Arial', 24, 'normal'))
    def upScore2(self):
        self.score2+=1
        self.clear()
        self.write(f"{self.score}     :     {self.score2}", align="center", font=('Arial', 24, 'normal'))
