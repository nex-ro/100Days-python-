from turtle import Turtle
class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", mode="r") as filetxt:
            if filetxt:
                self.highscore = int(filetxt.read())
            else:
                self.highscore = 0
        print(self.highscore)
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score :{self.score}  Highscore: {self.highscore}",align="center", font=('Arial', 24, 'normal'))

    def increment(self):
        self.score = self.score + 1
        if(self.score>self.highscore):
            self.highscore=self.score
            with open("data.txt", mode="w") as filetxt:
                filetxt.write(str(self.highscore))
                filetxt.close()

    def resetScore(self):
        self.score=0
        self.clear()
        self.write(f"Score :{self.score}  Highscore: {self.highscore}", align="center", font=('Arial', 24, 'normal'))

    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write(f"GameOVer", align="center", font=('Arial', 24, 'normal'))



