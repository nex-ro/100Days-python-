import data 
import os
import random 
logo='''
.__    .__       .__                   ____  .____                               
|  |__ |__| ____ |  |__   ___________ /  _ \ |    |    ______  _  __ ___________ 
|  |  \|  |/ ___\|  |  \_/ __ \_  __ \>  _ </\    |   /  _ \ \/ \/ // __ \_  __ \
|   Y  \  / /_/  >   Y  \  ___/|  | \/  <_\ \/    |__(  <_> )     /\  ___/|  | \/
|___|  /__\___  /|___|  /\___  >__|  \_____\ \_______ \____/ \/\_/  \___  >__|   
     \/  /_____/      \/     \/             \/       \/                 \/       

'''
vs='''
             
___  ________
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/ 
'''
def pickRandom():
    return random.choice(data.data)

winner=""
while(True):
    score=0
    status=True
    while(status):
        a=pickRandom()
        b=pickRandom()
        print(f"Compare A : {a['full_name']} ,{a['bio']}" )
        print(vs)
        print(f"Agaist B : {b['full_name']} ,{b['bio']}" )
        answ=input("Who has more followers? Type 'A' or 'B': ").lower()
        if(a['followers']>b['followers']):
            winner="a"
        else:
            winner="b"
        os.system('cls')
        if(answ==winner):
            score+=1
            print(f"You're right! Current score: ${score}.")
        else:
            status=False
            print(f"Sorry, that's wrong. Final score: {score}")
            

    again=input("Play again ? : answer with 'y' or 'n' :" )
    if(again=='n'):
        break

print("thank you for playing")