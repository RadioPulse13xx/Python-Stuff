#Programmer: John Henderson
#Program Name: The Museum Program
#Date: February 15, 2022

from operator import truediv


print("The Museum of Ancient Technology")
print()
 
age =int(input("Enter your age: "))
brochure = input("Would you like a brochure for $5.00?")
map = input("Would you like a map for $3.00? ")
    
if age <= 12:
    ticket_price = 4
    category = 'Child'
    tp = '$4.00'
elif age in range(13, 64) :
    ticket_price = 7
    category = 'Adult'
    tp = '$7.00'
elif age > 64:
    ticket_price = 5
    category = 'Senior'
    tp = '$5.00'


if brochure.startswith('y'):
    brochure_price = 5
    bp = '$5.00'
elif brochure.startswith('Y'):
    brochure_price = 5
    bp = '$5.00'
else :
    brochure_price = 0


if map.startswith('y'):
    map_price = 3
    mp = '$3.00'
elif map.startswith('Y'):
    map_price = 3
    mp = '$3.00'
else :
    map_price = 0


total = ticket_price + brochure_price + map_price
print()
print("Category:" ,'\t'+ category)
print("Ticket Price:",'\t'+ tp)
if brochure_price == 5:
    print("Brochure:", '\t' + bp)
if map_price == 3:
    print("Map: " , '\t', '\t'  + mp)

print()
print
total = str(total)
print('Total: ', '\t' + total)

