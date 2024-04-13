print("Welcome to the tip calculator!")
total= float( input("what was the total bill? $"))
tip=int(input("how much tip would you like to give? 10 , 12 , or 15?"))
people=int(input("how many people would to split the bill? "))
# count
total=total+total*(tip/100)
total=total/people
print("each people should pay "+str(total))