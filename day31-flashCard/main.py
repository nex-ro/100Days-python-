from tkinter import *
import pandas
import random
# public variable
BACKGROUND_COLOR = "#B1DDC6"
data=pandas.read_csv('data/cn_word.csv')
randomNum=random.randint(0,len(data))
canvas=None
photo=None

#correct button
def understand():
    global data
    data = data.drop(data.index[randomNum])
    data.to_csv("data/cn_word.csv", index=False)
    changeWord()


# change word
def changeWord():
    global randomNum
    global photo
    randomNum=random.randint(0,len(data))

    photo = PhotoImage(file="images/card_front.png")
    canvas.itemconfig(imageCanvas, image=photo)
    canvas.itemconfig(LgTxt, text="Chinese")

    canvas.itemconfig(logoTxt, text=data['hanyu'][randomNum])
    canvas.itemconfig(QuestionTxt, text=data['pinyin'][randomNum])
    window.after(1000,flipCard);


# balekKartu
def flipCard():
    global photo
    photo = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(imageCanvas,image=photo)
    canvas.itemconfig(LgTxt, text="English")
    canvas.itemconfig(logoTxt, text='')
    canvas.itemconfig(QuestionTxt, text=data['mean'][randomNum])


# ui

window=Tk()
window.title("Flash Card")
window.config(pady=50, padx=50)
window.configure(bg=BACKGROUND_COLOR)

canvas=Canvas(width=800 , height=526 ,highlightthickness=0)
photo=PhotoImage(file="images/card_front.png")
imageCanvas=canvas.create_image(400,263,image=photo)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0 , columnspan=2 )
# txt
LgTxt=canvas.create_text(400,140,text="chinese",font=("Ariel",40,"italic"))
logoTxt=canvas.create_text(400,220,text=data['hanyu'][randomNum],font=("Ariel",52,"bold"))
QuestionTxt=canvas.create_text(400,300,text=data['pinyin'][randomNum],font=("Ariel",60,"bold"))


photo2=PhotoImage(file="images/wrong.png")
WrongButton=Button(image=photo2,command=changeWord,highlightthickness=0)
WrongButton.grid(column=0, row=1 )

photo3=PhotoImage(file="images/right.png")
correctbutton=Button(image=photo3,command=understand,highlightthickness=0)
correctbutton.grid(column=1, row=1 )
timer = window.after(3000,flipCard);


window.mainloop()
