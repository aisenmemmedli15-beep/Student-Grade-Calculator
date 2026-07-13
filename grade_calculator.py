name=input("Enter student name: ")
score=float(input("Enter score: "))
if score>=90:
  grade="A"
elif score>=80:
  grade="B"
elif score>=70:
  grade="C"
elif score>=60:
  garde="D"
else:
  grade="F"
print("\nStudent: ", name)
print("Score:", score)
print("Grade:", grade)
