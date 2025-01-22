# What is the correct file extension for Python files?
# .py

# What is a correct command line syntax for checking if python is installed on your computer? (And also to check the Python version)
#python --version

# What is a correct syntax to exit the Python command line interface?
# exit()

# True or False: Indentation in Python is for readability only.
# False

# Insert the missing part of the code below to output "Hello World".
print("Hello World")

# Complete the code block, print "YES" if 5 is larger than 2. Hint: remember the indentation.
if 5 > 2:
    print("YES")

# Which character is used to define a Python comment:
# #

# Comments in Python are written with a special character, which one?
# This is a comment

# Use a multiline string to make the a multiline comment:
'''
This is a comment
written in 
more than just one line
'''

# What is a correct way to declare a Python variable?
x = 5

''' True or False:
You can declare string variables with single or double quotes. '''
x = "John"
# is the same as
x = 'John'

# True 

''' True or False:
Variable names are not case-sensitive. '''
a = 5
# is the same as
A = 5

# False

# Select the correct functions to print the data type of a variable:
myvar = 5
print(type(myvar))

# Which is NOT a legal variable name?
# my-var = 20

# Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"

# Create a variable named x and assign the value 50 to it.
x = 50

# What is a correct syntax to add the value 'Hello World', to 3 variables in one statement?
x = y = z = 'Hello World'

# Insert the correct syntax to assign values to multiple variables in one line: 
x, y, z = "Orange", "Banana", "Cherry"

# Consider the following code: What will be the result of a
fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)
# apple

# Consider the following code: What will be the printed result?
print('Hello', 'World')
# Hello World

# Consider the following code: What will be the printed result?
a = 'Hello'
b = 'World'
print(a + b)
# HelloWorld

# Consider the following code: What will be the printed result?
a = 4
b = 5
print(a + b)
# 9

# Consider the following code: What will be the printed result?
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
# Python is awesome

# Insert the correct keyword to make the variable x belong to the global scope. 
def myfunc():
   global x
   x = "fantastic"

# Consider the following code: What will be the printed result?
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
# Python is fantastic

# If x = 5, what is a correct syntax for printing the data type of the variable x?
x = 5
print(type(x))

# The following code example would print the data type of x, what data type would that be? 
x = 5
print(type(x))
# int   

# The following code example would print the data type of x, what data type would that be? 
x = "Hello World"
print(type(x))
# str

# The following code example would print the data type of x, what data type would that be? 
x = 20.5
print(type(x))
# float

# The following code example would print the data type of x, what data type would that be? 
x = ["apple", "banana", "cherry"]
print(type(x))
# list

# The following code example would print the data type of x, what data type would that be? 
x = ("apple", "banana", "cherry")
print(type(x))
# tuple 

# The following code example would print the data type of x, what data type would that be? 
x = {"name" : "John", "age" : 36}
print(type(x))
# dict

# The following code example would print the data type of x, what data type would that be? 
x = True
print(type(x))
# bool

# Which is NOT a legal numeric data type in Python:
# long

# Insert the correct syntax to convert x into a floating point number.
x = 5
x = float(x)

# Insert the correct syntax to convert x into a integer. 
x = 5.5 
x = int(x)

# Insert the correct syntax to convert x into a complex number. 
x = 5
x = complex(x)

# What will be the result of the following code:
print(int(35.88))
# 35

# What will be the result of the following code:
print(float(35))
# 35.0

# What will be the result of the following code:
print(str(35.82))
# 35.82 

# What will be the result of the following code:
x = 'Welcome'
print(x[3])
# c

# Use the len function to print the length of the string.
x = "Hello World"
print(len(x))

# Get the first character of the string txt.
txt = "Hello World"
x = txt[0]

# Insert the correct keyword to check if the word 'free' is present in the text:
txt = 'The best things in life are free!'
if 'free' in txt:
  print('Yes, free is present in the text.')

# What will be the result of the following code:
x = 'Welcome'
print(x[3:5])
# co

# Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]

#What will be the result of the following code:
x = 'Welcome'
print(x[3:])
# come 

# What is a correct syntax to print a string in upper case letters?
'Welcome'.upper()

# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

# Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()

# Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()

# Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")

# What is a correct syntax to merge variable x and y into variable z?
z = x + y

# What will be the result of the following code:
x = 'Welcome'
y = 'Coders'
print(x + y)
# WelcomeCoders

# Consider this code: What is a correct syntax to print 'Join the party'?
a = 'Join'
b = 'the'
c = 'party'
print(a + ' ' + b + ' ' + c)

# If x = 9, what is a correct syntax to print 'The price is 9.00 dollars'?
print(f'The price is {x:.2f} dollars')

# Insert the correct syntax to add a placeholder for the age parameter. 
age = 36
txt = f"My name is John, and I am {age}"
print(txt)

# What will be the result of the following code:
print(f'The price is {2 + 3} dollars')
# The price is 5 dollars