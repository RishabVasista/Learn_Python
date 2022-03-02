#Conditions:
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#1.if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

#2.elif 
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#3.else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#4.if and else w/o elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#5.short hand if
if a > b: print("a is greater than b")

#6.Short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

#7.One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#8.Test if a is greater than b, AND if c is greater than a (AND operation)
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#9.Test if a is greater than b, OR if a is greater than c (OR operation)
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#10.Nested if 
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")