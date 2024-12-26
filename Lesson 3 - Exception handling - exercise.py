# Question -1

a = 34
b = 44

#works normally 
print(float(a)

#valueerror
print(float(b))

# Question -2

# ImportError
# This error occurs when the Python interpreter is unable to import a particular name 
# or module within your code.

#parent.py
from child import testchild
testchild()

#child.py
def test_child():
       print('child')

#  open() function when trying to open a file that does not exist.
# IO Error

f = open ( "foo.txt", 'r' )

# name error
# A NameError in Python occurs when a program attempts to use a variable, 
# function, or module that is not defined or is not accessible in the current scope.

geeky = input()
print(geek)

# Division by zero

num1 = 10
num2 = 0
result = num1 / num2

# Question - 3

try: 
       numerator = int(input("Enter the numerator: "))
       denominator = int(input("Enter the denominator: "))

       # Check if the denominator is zero, if so raise the error
       if (denominator == 0):
           raise ValueError("You can't divide by zero")

       # Perform division
       result = numerator / denominator
       print(f"The result is: {result}")

except ValueError as e:
     print(f"Error: {e}")

# Question - 4

try: 
       numerator = int(input("Enter the numerator: "))
       denominator = int(input("Enter the denominator: "))
       
       assert denominator != 0
      
       # Perform division
       result = numerator / denominator
       print(f"The result is: {result}")

except AssertionError:
     print("You can't divide by zero")

#Question 5 & 6
# Theory Read from your text book

#Question 7
print ("Learning exception...")
try: 
       num1 = int(input("Enter the first number: "))
       num2 = int(input("Enter the second number: "))
       
       quotient = (num1 / num2)

       print ("Both the numbers entered were correct")
      

except ValueError:
     print("Please enter only numbers")
except ZeroDivisionError:
      print("Number 2 should not zero")
else:
      print(" Great .. you are a good programmer")
finally:
      print(" JOB OVER... Go Get SOME REST")

# Question 8


import math

try:
    result = math.pow(2, 2)  # pow() expects 2 arguments,
                            
except TypeError:
    print("Error has occurred math.pow()")
else:
    print("Result:", result)

try:
    result = math.sqrt(81)  # sqrt() expects 1 argument,
                           
except TypeError:
    print("Error has occurred math.sqrt()")
else:
    print("Result:", result)

# Question 9
# Refer Question 7

