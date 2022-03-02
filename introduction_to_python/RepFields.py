age=24
print("My age is "+str(24)+" years") # str() avoids error in this line

for i in range(1,13):
    print("No. {0} squared is {1} & cubed is {2}".format(i,i**2,i**3))
    #unformated

for i in range(1,13):
    print("No. {0:2} squared is {1:4} & cubed is {2}".format(i,i**2,i**3))
 # Right alligned

for i in range(1,13):
    print("No. {0:<2} squared is {1:<4} & cubed is {2}".format(i,i**2,i**3))
#left alligned

for i in range(1,13):
    print("No. {0:^2} squared is {1:^4} & cubed is {2}".format(i,i**2,i**3))
#centered

#precision
print("Pi is approximatey {0:12f}".format(22/7)) #min 6 digits spacing used
print("Pi is approximatey {0:12.50f}".format(22/7)) #ignores spacing as pi is too large