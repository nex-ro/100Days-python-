names_string=input("Whose ?\n")
names = names_string.split(",")
# names_string contains the input values provided. 
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
randomNum=random.randint(0,len(names)-1)
pick=names[randomNum]
print(f"{pick} is going to buy the meal today!")