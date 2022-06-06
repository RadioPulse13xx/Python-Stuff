#Programmer: John Henderson
#Program Name: The Vaccination Survey Program
#Date: February 22, 2022

print('The Vaccination Survey Program')
print()
n=int(input('How many people are in the survey? '))
print()

Moderna = 0
Pfizer = 0
none = 0
ages = []

for i in range(1,n + 1):
    print('Respondent ',i)
    print('------------')
    age=int(input('Age:'))
    ages.append(age)
    shot=input('Moderna, Pfizer, or None (M/P/N): ')

    if shot.startswith('m'):
        Moderna = Moderna + 1
    elif shot.startswith('M'):
        Moderna = Moderna + 1
    else :
        Moderna = Moderna + 0

    if shot.startswith('p'):
        Pfizer = Pfizer + 1
    elif shot.startswith('P'):
        Pfizer = Pfizer + 1
    else :
        Pfizer = Pfizer + 0

    if shot.startswith('n'):
        none = none + 1
    elif shot.startswith('N'):
        none = none + 1
    else :
        none = none + 0
    print()

print('Summary')
print('------')
print('Respondents:', '\t', n)
print('Moderna: ', '\t', Moderna )
print('Pfizer:', '\t', Pfizer)
print('None:', '\t', '\t', none)
print('%s \t %2.f' % ('Average age:', sum(ages)/len(ages)))
print('Youngest:', '\t', min(ages))
print('Oldest:', '\t', max(ages))

