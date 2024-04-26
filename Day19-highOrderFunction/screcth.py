import turtle as tim

turtle=tim.Turtle()
scree=tim.Screen()
turtle.forward(10)



def forward():
    turtle.forward(10)

def back():
    turtle.back(10)

def clockw():
    newHead=tim.heading() -10
    turtle.setheading(newHead)

def conterclock():
    newHead=tim.heading()+10
    turtle.setheading(newHead)

scree.listen()
scree.onkey(forward,"w")
scree.onkey(scree.resetscreen,"c")
scree.onkey(back,"s")
scree.onkey(clockw,"d")
scree.onkey(conterclock,"a")
scree.exitonclick()