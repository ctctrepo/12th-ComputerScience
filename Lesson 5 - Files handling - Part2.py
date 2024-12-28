# tell method
f = open("test.txt", "rb")
# print(f.tell())
# print(f.read())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

#seek beginning of the file(0)
f = open("test.txt", "rb")
print(f.tell())
f.seek(7,0)
print(f.read()) 

#seek current position of the file
f = open("test.txt", "rb")
print(f.readline())
f.seek(14,1)
print(f.read()) 

f = open("test.txt", "rb")
print(f.readline())
print(f.readline())
f.seek(11,1)
print(f.read()) 


# seek end of file(2)
f = open("test.txt", "rb")
print(f.tell())
f.seek(9,2)
print(f.read())

