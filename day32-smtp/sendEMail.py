import smtplib

# setup
myEmail="deri22ti@mahasiswa.pcr.ac.id"
passsword="fshxinxwpnaswcxk"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=myEmail,password=passsword)
    connection.sendmail(
        from_addr=myEmail,
        to_addrs="derixkho@gmail.com",
        msg="Subject:hello test \n\nThis is the body of my email"
    )



