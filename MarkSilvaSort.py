print("The Sort 3 Numbers Program")
print()
a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
c = int(input("Enter an integer: "))
print()
print("Original Order:",a,b,c)
scores = [a,b,c]
scores.sort()
print("Sorted Order:",*scores)