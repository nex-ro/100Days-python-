import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
Player=Player()
game_is_on = True
CarList=[]
Scoreboard=Scoreboard()
n=0
def restart():
    for car_manager in CarList:
        car_manager.reset()
        car_manager.hideturtle()
    CarList.clear()
    Player.goto(0, -280)
    CarManagers.levelUp()
while game_is_on:
    delete=[]
    if(n%6==0):
        CarManagers = CarManager()
        CarList.append(CarManagers)
    for i in range(len(CarList)):
        CarList[i].move()
        if(CarList[i].distance(Player)<25):
            Scoreboard.gameOver()
            game_is_on=False
            break;
        if(CarList[i].xcor() < -330):
            # CarList[i].reset()
            delete.append(CarList[i])
    for j in range(len(delete)):
        CarList.remove(delete[j])

    time.sleep(0.1)
    screen.update()
    screen.onkey(Player.moveF,"Up")
    if(Player.ycor()>280):
        Scoreboard.levelUp()
        restart()


    n=n+1


screen.exitonclick()