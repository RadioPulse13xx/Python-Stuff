print('The Factorial Program')
print()
n=int(input('Enter and integer: '))
factorial = 1
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print(n,"factorial is",factorial)