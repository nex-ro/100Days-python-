import random
from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=500,height=400)
colors=['red','blue','yellow','green','purple','salmon']
userBet=screen.textinput("Make A Bet", "input a color that you bet will win(red,blue,yellow,green,purple,salmon)")
turtlees=[]

def randomMove(turtle):
    movee=random.randint(5,20)
    turtle.forward(movee)

for i in range(6):
    timmy=Turtle()
    timmy.shape('turtle')
    turtlees.append(timmy)
    timmy.penup()
    timmy.color(colors[i])
    timmy.setposition(x=-200,y=-100 +(i*40))
isRaceOn=True
while(isRaceOn):
    for i in range(len(turtlees)):
        randomMove(turtlees[i])
        if(turtlees[i].xcor()>=230):
            isRaceOn=False
            print(f"{colors[i]} win ")
            if(userBet.lower()==colors[i]):
                print("you Win")
            else:
                print("you Lose")
            break;


screen.exitonclick()
