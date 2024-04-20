import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hands=[]
bot=[]

logo='''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/
'''

def generated(list):
    if(len(list)==0):
        list.append(random.choice(cards))
    else:
        generate=random.choice(cards)
        if(generate+list[0]>21):
            list.append(1)
        else:
            list.append(generate)

def sumAll(list):
    sum=0
    for i in list:
        sum+=int(i)
    return sum
        
pilihan=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while(pilihan=='y'):
    hands=[]
    bot=[]
    os.system('cls')
    status=True
    print(logo)
    generated(hands)
    generated(hands)
    generated(bot)
    generated(bot)
    print(f"Your cards:{hands}, current score: {sumAll(hands)}")
    print(f"computer first cards:{bot[0]}")
    if(sumAll(hands)==21):
        print(f"You Win You got a blackjack(21) with card {hands}")
        status=False

    elif(sum(bot)==21):
        print(f"Computer win , computer got blackjack(21) with card {bot}")
        status=False
    else:
        ambil=input("Type 'y' to get another card, type 'n' to pass:")
        while(ambil=='y'):
            generated(hands)
            if(sumAll(hands)>21):
                print(f"You lost , you've busted your card {hands}")
                ambil='n'
                status=False
            else:
                print(f"Your cards:{hands}, current score: {sumAll(hands)}")
                print(f"computer first cards:{bot[0]}")
                ambil=input("Type 'y' to get another card, type 'n' to pass:")
        while(sumAll(bot)<=16 and status==True):
            generated(bot)
        if(sumAll(bot)>21 and status==True):
            status=False
            print(f"You win with cause computer busted with card {bot} \n and card {hands} and total value {sumAll(hands)}")
            
            status=False
        elif(status==True):
            if(sumAll(bot)>sumAll(hands)):
                print(f"Computer win with card {bot} and value {sumAll(bot)} \n while your card {hands} and total value {sumAll(hands)}")
                status=False
            elif(sumAll(hands)>sumAll(bot)):
                print(f"You win with card {hands} and total value {sumAll(hands)}\n while Computer card {bot} and total value {sumAll(bot)}")
            elif(sumAll(hands)==sumAll(bot)):
                print(f"TIE ! , bot of computer and you got total value ${sumAll(bot)} your card is ${hands} and computer card is ${bot}")
    pilihan=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    
   
    
