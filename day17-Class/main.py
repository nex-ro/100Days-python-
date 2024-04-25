from data import  question_data
from quizModel import model
from brain import brain

model=model()
brain=brain()

for i in question_data['results']:
    answ=model.AskQuestion(i).lower()
    brain.checkAnsw(answ,i)

brain.complate()
