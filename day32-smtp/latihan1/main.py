import datetime as dt
import smtplib
import random
# setup
myEmail="deri22ti@mahasiswa.pcr.ac.id"
passsword="fshxinxwpnaswcxk"
now=dt.datetime.now()
def sendMail(email_Target):
    with open('quotes.txt', 'r') as txt:
        content =txt.readlines()
        randomInt = random.randint(0, len(content) - 1)
        quotes=content[randomInt]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=myEmail,password=passsword)
            connection.sendmail(
                from_addr=myEmail,
                to_addrs=email_Target,
                msg=f"Subject:Have a good day \n\n{quotes}"
            )
if(now.weekday()==0):
    sendMail(email_Target="derixkho@gmail.com")