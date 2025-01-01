fileobject = open("hello.txt", "a")
fileobject.write("Welcome my class\n")
fileobject.write("It is a fun place\n")
fileobject.write("You will learn and play\n")
fileobject.close()

fileobject = open("hello.txt", "r")
str = fileobject.readline()
while str:
    print(str)
    str = fileobject.readline()
fileobject.close()

fileobject=open("empfile.txt","w")
print("Enter END to stop the process" )
while True:
    str=input("Enter a string/sentence  : ")
    if (str.lower() == "end"):
        break
    fileobject.write(str + "\n")
fileobject.close()

fileobject = open("empfile.txt", "r")
str = fileobject.readline()
while str:
    if (str[0].isupper()):
         print(str)
    str = fileobject.readline()
fileobject.close()


import pickle
print("WORKING WITH BINARY FILES")
bfile=open("item.dat","ab")
recno=1
print ("Enter Items")
print()
#taking data from user and dumping in the file as list object
while True:
    print("RECORD No.", recno)
    ino=int(input("\tItem no : "))
    iname=input("\tItem Name : ")
    iquantity=int(input("\tQuantity: "))
    iprice=float(input("\tPrice : "))
    amount=iquantity*iprice
    print("\tTOTAL AMOUNT : ", amount)
    idata=[ino,iname,iquantity,iprice,amount]
    pickle.dump(idata,bfile)
    ans=input("Do you wish to enter more records (y/n)? ")
    recno=recno+1
    if ans.lower()=='n':
        print("Record entry OVER ")
        print()
        break
bfile.close()

import pickle
print("Now reading the employee records from the file")
print()
readrec=1
try:
    with open("item.dat","rb") as bfile:
        while True:
            itemdata=pickle.load(bfile)
            print("Record Number : ",readrec)
            print("\t\tItem No:", itemdata[0])
            print("\t\tItem Name:",itemdata[1])
            print("\t\tQuantity:",itemdata[2])
            print("\t\tPrice per item:", itemdata[3])
            print("\t\tAmount:",itemdata[4])
            readrec=readrec+1
except EOFError:
   pass

