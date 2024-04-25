class brain():
    score = 0
    done = 0
    def checkAnsw(self,answ,object):
        self.done=self.done+1
        if(answ==object['correct_answer'].lower()):
            print("You got it right!")
            self.score=self.score+1
            print("The correct answer was: True.")

        else:
            print("That's wrong")
            print("The correct answer was: False.")
        print(f"Your current score : {self.score}/{self.done}\n\n")

    def complate(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.done}")