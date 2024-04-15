# Input a list of student scores
student_scores = input().split()
highest=0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if(student_scores[n]>highest):
    highest=student_scores[n]
# Write your code below this row 👇
print(f"The highest score in the class is: {highest}")
