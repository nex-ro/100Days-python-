import pandas
import datetime
import smtplib
import random
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pickRandomLatter(name,email):
    randomInt=random.randint(1,3)
    with open(f'letter_templates/letter_{randomInt}.txt', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('[NAME]', name)
    sendMail(addressMail=email,txt=filedata)


# 4. Send the letter generated in step 3 to that person's email address.
def sendMail(addressMail,txt):
    myEmail = "deri22ti@mahasiswa.pcr.ac.id"
    passsword = "fshxinxwpnaswcxk"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myEmail, password=passsword)
        connection.sendmail(
            from_addr=myEmail,
            to_addrs=addressMail,
            msg=f"Subject:HAPPY BIRTHDAY \n\n{txt}"
        )

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# ask input :
# name=input(f"whose birthday :")
# email=input(f"what {name} email :")
# year=input(f"what {name} born's year :")
# month=input(f"what {name} born's month :")
# day=input(f"what {name} born's day :")
#
# newData={
#     'name':name,
#     'email':email,
#     'year':year,
#     'month':month,
#     'day':day,
# }
# data=pandas.read_csv("birthdays.csv")
# data_frame = pandas.DataFrame([newData])
# data_frame = pandas.concat([data, data_frame], ignore_index=True)
#
# data_frame.to_csv('birthdays.csv',index=False)
# 2. Check if today matches a birthday in the birthdays.csv
data=pandas.read_csv("birthdays.csv")
now=datetime.datetime.now()
for i in range(len(data['name'])):
    if(data['month'][i]==now.month and data['day'][i]==now.day):
        text=pickRandomLatter(data['name'][i],email=data['email'][i])







