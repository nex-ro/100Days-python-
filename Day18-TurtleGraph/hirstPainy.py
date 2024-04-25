import random

import colorgram
import turtle as t
t.colormode(255)

listt=[]
# Extract 6 colors from an image.
colors = colorgram.extract('paint.jpg', 40)

for i in range(len(colors)):
    R=colors[i].rgb.r
    G = colors[i].rgb.g
    B = colors[i].rgb.b
    newColor=(R,G,B)
    listt.append(newColor)
t.shape("classic")

for i in range(10):
    for j in range(10):
        t.penup()
        t.setposition(-310 + (j * 70), -250 + (i * 70))
        t.pendown()
        t.begin_fill()
        t.dot(40,random.choice(listt))
        t.end_fill()





S=Screen()
S.exitonclick()