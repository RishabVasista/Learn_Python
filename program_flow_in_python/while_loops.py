#1.Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1

#2.Exit the loop when i is 5. (break in while loop)

i = 1
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1

#3.Continue to the next iteration if i is 7 i.e don't print 7 (continue in while loop)
i = 0
while i < 10:
  i += 1
  if i == 7:
    continue
  print(i)

#4.Print a message once the condition is false (else in a while loop)

i = 1
while i < 7:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#5.Print numbers including pass statements (pass in while loop)

i = 1
while i < 5:
  print(i)
  if i == 3:
      pass
  i += 1

#6. Print the sum of first 10 natural numbers
n = 10
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    
print("The sum is", sum)

#7.Printing a statement n times:
n=int(input("Enter n:"))
s=input("Enter statement:")
print ("")
i=0
while i<n:
    print (s)
    i=i+1

#8.Print all letters except 'x' and 'y':
i = 0
a = 'xxdaxtaxydyexcyoxxdyyex'
 
while i < len(a):
    if a[i] == 'x' or a[i] == 'y':
        i += 1
        continue
         
    print(a[i])
    i += 1

#9.input in while loop:
a = int(input('Enter a number (4) to quit): '))
 
while a != 4:
    a = int(input('Enter a number (4 to quit): '))

#10.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
i = 1500
n = 2700
while i<=n :
    if i%7 == 0 and i%5 == 0:
        print(i)
    i=i+1
