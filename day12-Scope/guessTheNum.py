import random
logo='''

                                        __  .__                                 ___.                 
   ____  __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
  / ___\|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
 / /_/  >  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \___  /|____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
/_____/             \/     \/     \/             \/     \/       \/            \/    \/     \/       
'''

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
hp=0
difficulty=input("Choose a diffulty. type 'easy' or 'Hard :'").lower()
if(difficulty=="hard"):
    hp=5
else:
    hp=10
answ=random.randint(1,100)

for i in range(hp):
    print(f"You have {hp} attempts remaining to guess the number.")
    
    guess=int(input("Make a guess: "))
    if(guess==answ):
        print(f"You got it! The answer was {answ}.")
        break
    elif(guess>answ):
        print("Too High")
    elif(guess<answ):
        print("Too Low")
    else:
        print("your input incorect")
    print("tryAgain")
    hp-=1

