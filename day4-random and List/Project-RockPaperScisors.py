import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pick=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print(pick[choice])
computer=""
randomNum=random.random()*4
if(randomNum<=1):
    computer=rock
elif(randomNum>1 and randomNum<=1):
    computer=paper
else:
    computer=scissors
print(computer)

if(pick[choice]==scissors):
    if(computer==paper):
        print("You win")
    elif(computer==scissors):
        print("You Tie")
    else:
        print("you Lose")
elif(pick[choice]==rock):
    if(computer==scissors):
        print("You win")
    elif(computer==rock):
        print("You Tie")
    else:
        print("you Lose")
if(pick[choice]==paper):
    if(computer==rock):
        print("You win")
    elif(computer==paper):
        print("You Tie")
    else:
        print("you Lose")



