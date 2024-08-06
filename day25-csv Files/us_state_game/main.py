import turtle
import pandas
screen =turtle.Screen()
screen.title("US States Games")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess =[]
data=pandas.read_csv('50_states.csv')
data_disc=data.to_dict()
while(len(guess)<len(data_disc['state'])):
    answ = turtle.textinput(title="Guess the states", prompt="whats another states's name").capitalize()
    if (len(data[data.state == answ]) > 0 and answ not in guess):
        dataState = data[data.state == answ]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(dataState.x.item(), dataState.y.item())
        t.write(answ)
        guess.append(answ)
        print(guess)
    else:
        print("wrong")

screen.exitonclick()