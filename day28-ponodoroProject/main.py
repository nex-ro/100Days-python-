import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
set=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def resetCount():
    labelstatus.config(text="Timer", fg="#000")
    window.after_cancel(timer)
    labelCheck.config(text="")
    global set
    set=0
    canvas.itemconfig(textCanvas,text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def countDownStart():
    global set
    set = set + 1
    canvas.itemconfig(textCanvas,text="00:00")
    longDuration=LONG_BREAK_MIN*60
    shortDuration=SHORT_BREAK_MIN*60
    work=WORK_MIN*60
    if(set%8==0):
        countDown(longDuration)
        labelstatus.config(text="Break" ,fg=RED)
    elif(set%2==1):
        countDown(work)
        labelstatus.config(text="WORK", fg=GREEN)
    elif(set%2==0):
        countDown(shortDuration)
        labelstatus.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    global set
    hr,minute=divmod(count,60)
    canvas.itemconfig(textCanvas,text=f"{hr:02d}:{minute:02d}")
    if(count>=0):
        global timer
        timer=window.after(1000,countDown,count-1);
    else:
        textCheck=''
        for i in range(int(math.floor(set/2))):
            textCheck+="✓"
        labelCheck.config(text=textCheck)
        countDownStart()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomorodo")
window.minsize(width=300 , height=100)
window.config(pady=100, padx=50 ,bg=YELLOW)
labelstatus=Label(text="Timer" ,font=(FONT_NAME,"36",'bold'),fg=GREEN ,bg=YELLOW)
labelstatus.grid(column=1,row=0)

canvas=Canvas(width=220 , height=224 ,bg=YELLOW ,highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvas.create_image(110,112,image=photo)
textCanvas=canvas.create_text(110,130,text="00.00" ,font=(FONT_NAME,"24","bold"))
canvas.grid(column=1, row=1)

buttonStart=Button(text="Start" ,command=countDownStart)
buttonStart.grid(column=0 ,row=3)

labelCheck=Label(text="" ,fg=GREEN ,bg=YELLOW,font=(FONT_NAME,"12","bold"))
labelCheck.grid(column=1,row=2)



buttonReset=Button(text="reset" ,command=resetCount)
buttonReset.grid(column=2 ,row=3)


window.mainloop()