#Write a program to select a list of options, and allow the user to select an option from the list.
#they should be numbered from 1 to 9 and include atleast 4 options with 0 as exit

while True:
    print('Please choose an option from the list below:')
    print('1.Play Valorant')
    print('2.Go cycling')
    print('3.Learn Python')
    print('4.Extract Invoices')
    print('0.EXIT')
    a=input()
    if str(a) == '0':
        break
    elif a in '1234':
        print ('You have selected {}'.format(a))    
    else:
        print("try again")    
