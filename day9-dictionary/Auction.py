import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print("Welcome to the auction")
bid=[]
def addBid(nama,amount):
    bid.append({
        "nama": nama,
        "bid": amount,
    })

    

def countWinner():
    highest=0
    bidder=""
    if(len(bid)!=0):
        for i in range(len(bid)):
            if(int(bid[i]['bid'])>highest):
                highest=bid[i]['bid']
                bidder=bid[i]['nama']
        print(f"The bid goes to {bidder} with ${highest}")
    else:
        print(f"The bid goes to no one")
        
while(True):
    nama=input("What is your name ?:")
    amount=input("what is your bid?: $")
    status=input("are there any other bidders? Type 'yes or 'no'")
    addBid(nama,amount)
    if(status=="no"):
        countWinner()
        break
    else:
        os.system('cls')
