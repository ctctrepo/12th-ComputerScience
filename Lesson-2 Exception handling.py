a = 34
b = "test"

#works normally 
print(float(a))

#valueerror
print(float(b))


#  ----------------------------------------------
a = 34
b = "test"

try:
#works normally 
    print(float(a))

#valueerror
    print(float(b))
except ValueError as e:
    raise Exception('The value error occurred') from None

except :
    raise Exception("Some other syntax error has occured") from None

else:
    print("No error")

#------------------------------------------------------------------------------------

# assert  Debugging tools that help in the smooth flow of code.

# initializing number
a = 4
b = 0
 
# using assert to check for 0
print("The value of a / b is : ")
assert b != 0
print(a / b)

#------------------------------------------------------------------------------

# finally The finally block, if specified, 
# will be executed regardless if the try block raises an error or not.

a = 34
b = "test"

try:
#works normally 
    print(float(a))

#valueerror
    print(float(b))
except ValueError as e:
    raise Exception('The value error occurred') from None

except :
    raise Exception("Some other syntax error has occured") from None

# else:
#     print("No error")

finally:
  print("End")

