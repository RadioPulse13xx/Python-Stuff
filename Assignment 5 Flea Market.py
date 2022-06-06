import sys


try:
    df = open('Final.txt','r')
    for_sale=df.read()
    for_sale=eval(for_sale)
    df.close
except IOError:
    for_sale={}

    
while True:
    try:
        print("\n" * 30)
        print("=======================")
        print(" Flea Market Menu")
        print("-----------------------")
        print()
        print("1 - Add an item")
        print("2 - Delete an item")
        print("3 - Search for an item")
        print("4 - Change the price of an item.")
        print("5 - View Dictionary")
        print("6 - Save Dictionary")
        print("7 - Exit")
        print()

        choice = int(input("Your choice: "))

        print()

        if choice == 1:
            name = input("Enter an Item: ")
            for_sale[name]=float(input("Enter a price: "))
            print()
            modify = + 1


        elif choice == 2:
            name = input("Enter an Item: ")
            print()
            if name in for_sale:
                del for_sale[name]
                print(name, "has been deleted.")
                print()
                modify = + 1
            else:
                print(name, "was not found.")
                print()


        elif choice == 3:
            name = input("Enter an Item: ")
            if name in for_sale:
                print("Price: ",for_sale[name])
                print()
            else:
                print()
                print(name,"not found.")
                print()


        elif choice == 4:
            name = input("Enter an Item: ")
            if name in for_sale:
                print()
                print("The price of ", name, "is", for_sale[name])
                print()
                value = float(input("Enter new price: "))
                print()
                for_sale[name] = value
                modify = + 1
            else:
                print(name,"not Found")


        elif choice == 5:
            if bool(for_sale) == False:
                print('Dictionary is empty')
                print()
            else:
                print('Current Dictionary',)
                print('==================',)
                print()
                print('Item','\t', '\t', 'Price')
                print('----', '\t', '\t', '-----')
                for k in for_sale:
                    print('%-15s %6.2f' % (k, for_sale[k]))
                print()


        elif choice == 6:
            modify = 0
            try:
                f = open("Final.txt","wt")
                f.write(str(for_sale))
                f.close()
                print('The dictionary was saved')
                print()
            except:
                print("Unable to write to file")


        elif choice == 7:
            try:
                if modify > 0:
                    save = input('Save your work(Y/N)')
                    if save.startswith('y'):
                        f = open("Final.txt","wt")
                        f.write(str(for_sale))
                        f.close()
                        print('The dictionary was saved')
                        print()
                        sys.exit()
                    elif save.startswith('Y'):
                        f = open("Final.txt","wt")
                        f.write(str(for_sale))
                        f.close()
                        print('The dictionary was saved')
                        print()
                        sys.exit()
                    else:
                        print('Work not saved')
                        print()
            except NameError:
                print()
                break
            else:
                break


        else:
            print("Invalid choice. Valid choices are 1 to 7.")
            print()
        a = input("Press ENTER to continue...")


    except ValueError:
        print("That's not an integer.")
        print()
        a = input("Press ENTER to continue...")