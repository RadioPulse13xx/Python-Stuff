students = {'Bob': 88, 'Lucy':79, 'Tracey':94}

choice = 0
while choice != 3:
    print("\n" * 30)
    print("=======================")
    print(" Intro to Tardigrades")
    print("-----------------------")
    print()
    print("1 - Add student")
    print("2 - Display all students")
    print("3 - Quit menu")
    print()

    choice = int(input("Your choice: "))
    
    print()
    if choice == 1:
        name = input("Name: ")
        students[name]=int(input("Score: "))
        pair = list(students.items()) [-1]
        print()
        print('New Student Information')
        print()
        print('Name','\t','Score')
        print('----','\t','-----')
        print (*pair, sep=' '*8)
    elif choice == 2:
        print('Name','\t','Score')
        print('----','\t','-----')
        for k in students:
            print('%s \t %5s' % (k,students[k]))
        print()
    elif choice == 3:
        break
    else:
        print("Not a valid choice.")
    print()
    a = input("Press ENTER to continue...")