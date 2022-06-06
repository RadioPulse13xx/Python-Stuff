print("The Pass or Fail Program")
print()
first=str(input("Please enter your first name: "))
mid_score=float(input("Please enter your midterm score: "))
final_score=float(input("Please enter your final score: "))
lab_score=float(input("Please enter your lab score: "))
print()
m=float(mid_score)
f=float(final_score)
l=float(lab_score)
avg = ((m + f + l) / 3)

if avg > 70:
    grade = 'pass'
else: 
    grade = 'fail'


print('Name: ', '\t', '\t', first)
avg =str(avg)
print('Average: ','\t', avg)
print('Grade: ','\t', grade)

