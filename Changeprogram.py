print("The Average Calculation Program")
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
print('\t %s \t %16s \t %8s \t %8s \t %8s' % ('Name', 'Midterm', 'Final', 'Lab', 'Average'))
print('\t %s \t %s \t %s \t %s \t %s' % ('--------', '--------', '--------', '--------', '--------'))
print('\t %s \t %16.2f \t %8.2f \t %8.2f \t %8.2f' %  (first, mid_score, final_score, lab_score, avg))

