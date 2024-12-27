# open 
f = open("test.txt", "r")
print(f.read())
f.close()

# open a file in different directory
f = open("E:\\Training\\Python\\Youtube Videos - Python\\GIT\\Lesson -4\\Myfiles\\demo.txt", "r")
print(f.read())
f.close()

# escape character

# "Hello  \"python\" from the trainer"


# opening a file using with clause , the file is closed automatically
with open("test.txt","r") as f:
   file_content = f.read()
   print(file_content)

# write
f = open("test.txt", "w")
f.write("Hello how are you\n")
f.close()

# write numeric data
f = open("numeric.txt", "w")
mark=75
f.write(str(mark))
f.close()

#writeline 
f = open("test.txt", "w")
content = ["Hello\n","Good morning\n","Good luck\n","Thank you\n"]
f.writelines(content)
f.close()

#append a file
file = open('test.txt', 'a')
file.write("Regards\n")
file.close()

#read in binary
file = open("test.txt", "rb")
content = file.read()
print(content)
file.close()

# read specified number of bytes
file = open("test.txt", "r")
content = file.read(10)
print(content)
file.close()

# negative or no argument, the entire content is read
file = open("test.txt", "r")
content = file.read(-5) # .read()
print(content)
file.close()

# readline(single line) and readlines(multiple lines)
file = open("test.txt", "r")
content = file.readline()  #readlines
print(content)
file.close()

#split the lines
file = open("test.txt", "r")
content = file.readlines()
for line in content:
    word = line.split()
    print(word)
file.close()
