# Write your code below this line 👇
import math
def paint_calc(h,w,c):
  res=(math.ceil(h*w/c))
  print(f"You'll need {res} cans of paint.")
  


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(test_h, test_w, coverage)
