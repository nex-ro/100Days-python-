from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def randomPass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password =[]
    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    for x in range (0,nr_letters):
        if(nr_numbers!=0):
              for y in range(nr_numbers):
                    password.append(random.choice(numbers))
                    nr_numbers-=1
        elif(nr_symbols!=0):
            for z in range(0,nr_symbols):
                password.append(random.choice(symbols))
                nr_symbols-=1
        else:
            password.append(random.choice(letters))
    random.shuffle(password)
    randPass=''.join(password)
    inputanPASS.insert(0,randPass)
    pyperclip.copy(randPass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePass():
    password=inputanPASS.get()
    web=inputanWeb.get()
    email=inputanEmail.get()
    newData={
        web:{
        "email":email,
        "password":password,
        }
    }
    if(inputanWeb.get()=='' or inputanPASS==''):
        messagebox.showinfo(title="Information",message="Please dont let any entry is empty")
    else:
        isOkay=messagebox.askokcancel(title="is it okay" ,message=f"is it okay ? \nWebsite : {web}\nEmail:{email}\n Pass :{password} \n" )
        if isOkay:
            try:
                # Reading data from the file
                with open("data.json", "r") as file1:
                    data = json.load(file1)
            except FileNotFoundError:
                # If file not found, initialize the data
                data = {}

            # Update the data
            data.update(newData)

            # Writing data to the file
            with open("data.json", "w") as file1:
                json.dump(data, file1, indent=4)

            # Clear the input fields
            inputanWeb.delete(0, END)
            inputanPASS.delete(0, END)




# ---------------------------- Search method ------------------------------- #

def search():
    website = inputanWeb.get()
    try:
        with open("pass.json", "r") as file1:  # Ensuring the file name matches the saving part
            data = json.load(file1)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website].get('email', 'No email found')
            password = data[website].get('password', 'No password found')
            messagebox.showinfo(title="Data Information",
                                message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No Data Found for this Website")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas=Canvas(width=200 , height=200  )
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1, row=0 )


label1=Label(text="webiste:")
label1.grid(column=0 ,row=1)
label2=Label(text="Email/Username:")
label2.grid(column=0 ,row=2)
label3=Label(text="Password:")
label3.grid(column=0 ,row=3)


inputanWeb=Entry(width=35)
inputanWeb.grid(column=1,row=1 )
inputanWeb.focus()
search=Button(text="Search",width=21 ,command=search)
search.grid(column=2,row=1)

inputanEmail=Entry(width=35)
inputanEmail.grid(column=1,row=2 ,columnspan=2)
inputanEmail.focus()
inputanEmail.insert(0,"derixkho@gmail.com")
inputanPASS=Entry(width=21 )
inputanPASS.grid(column=1,row=3 ,columnspan=1)
inputanPASS.focus()


ButtonGenerate=Button(text="Generate Password" ,command=randomPass,width=21)
ButtonGenerate.grid(column=2,row=3)
addButton=Button(text="Add",width=36 ,command=savePass)
addButton.grid(column=1,row=4,columnspan=2)

window.mainloop()