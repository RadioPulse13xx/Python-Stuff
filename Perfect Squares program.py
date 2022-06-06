print('The Perfect Squares Program')
print()
n=int(input('How many perfect squares? '))
print()
print('\t','       ', '\t', 'Perfect')
print('\t','Integer', '\t', ' Square')
print('\t','-------', '\t', ' ------')
for i in range(1,n+1):
    print('\t %7s \t %7s' % (i,i*i))
