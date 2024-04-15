target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total=0
for x in range(1,target+1):
  if(x%2==0):
    total+=x

print(total)