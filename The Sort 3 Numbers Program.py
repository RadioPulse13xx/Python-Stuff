print('The Sort 3 Numbers Program')
print()
a=int(input('Enter an integer:'))
b=int(input('Enter an integer:'))
c=int(input('Enter an integer:'))
x=[a,b,c]
x.sort (reverse=False)
print()
print('Original order: ',a,b,c)
print('Sorted order: ',*x)