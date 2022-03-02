#1.Print each fruit in a list (looping through a list)
fruits = ["apple", "banana", "cherry", "lychee", "pineapple"]
for i in fruits:
  print(i)

#2.Print each letter of the word potato (looping through a string)
for i in "potato":
    print (i)

#3.Exit the loop when x is "Potato" (break in for loop)

fruits = ["apple", "banana", "cherry", "lychee","Potato" ,"pineapple"]
for i in fruits:
  print(i)
  if i == "Potato":
    break

#4.skip potato in the above code (continue in for loop)
fruits = ["apple", "banana", "cherry", "lychee","Potato" ,"pineapple"]
for i in fruits:
  if i == "Potato":
    continue
  print(i)  

#5.Using range in for loops
for i in range(1, 9):
  print(i)

#6. Using range in inceremented steps in for loops
for i in range(1,100,10):
  print(i)

#7.Print all numbers from 0 to 5, and print a message when the loop has ended. (else in for loop)

for i in range(10):
  print(i)
else:
  print("Completed")

#8.Nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#9.pass in for loop
for x in [0, 1, 2]:
  pass

#10.Program to print table of given number.

n = int(input("Enter the number "))  
for i in range(1,11):  
    c = n*i  
    print(n,"*",i,"=",c)  