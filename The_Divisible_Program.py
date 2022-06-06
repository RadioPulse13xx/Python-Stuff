print()
print("The Divisible Program")

yeet = True
while(yeet == True):
    try:
        print()
        num = int(input("Please enter an integer: "))

        if num%2 == 0:
            print("\t Divisible by 2.")
        if num%3 == 0:
            print("\t Divisible by 3.")
        if num%6 == 0:
            print("\t Divisible by 6.")
        yeet = False
    except ValueError:
            print("\t That's not an integer.")
