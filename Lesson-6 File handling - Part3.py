#Creating and traversing a text file

# w+ reading and writing # w writing only
fileobject = open("practice.txt", "w+")
while True:
    data = input("Enter data to save in the text file : ")
    fileobject.write(data)
    ans = input("Do you wish to enter more data?(y/n) : ")
    if (ans == 'n'):
        break
# fileobject.seek(0)
# print(fileobject.read())
fileobject.close()

# display data from a text file
fileobject = open("practice.txt", "r")
str = fileobject.readline()
while str:
    print(str)
    str = fileobject.readline()
fileobject.close()

# Read and write Operation in a text file
fileobject = open("report.txt", "w+")
print("Writing data in the file")
print()
while True:
   line = input("Enter a sentence ")
   fileobject.write(line)
   fileobject.write('\n')
   choice = input("Do you wish to enter more data? (y/n) : ")
   if (choice in ('n','N')) : 
        break
print("The byte position of file object is ",fileobject.tell())
fileobject.seek(0)
print()
print("Reading data from the file")
str = fileobject.read()
print(str)



 
