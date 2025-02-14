# List - multiple items in a single variable.
color = ["red", "blue", "green"]
print(color)
print(color[0])

#pickling using dump method
import pickle
listvalues = [1,"Geetika",'F',26]
fileobject = open("mybinary.dat","wb")
pickle.dump(listvalues,fileobject)
fileobject.close()

#unpickling using load method
import pickle
print("The data that were stored in file area: ")
fileobject = open("mybinary.dat","rb")
objectvar = pickle.load(fileobject)
fileobject.close()
print(objectvar)

#Write a employee record in  a binary file
import pickle
print("WORKING WITH BINARY FILES")
bfile=open("empfile.dat","ab")
recno=1
print ("Enter Records of Employees")
print()
#taking data from user and dumping in the file as list object
while True:
 print("RECORD No.", recno)
 eno=int(input("\tEmployee number : "))
 ename=input("\tEmployee Name : ")
 ebasic=int(input("\tBasic Salary : "))
 allow=int(input("\tAllowances : "))
 totsal=ebasic+allow
 print("\tTOTAL SALARY : ", totsal)
 edata=[eno,ename,ebasic,allow,totsal]
 pickle.dump(edata,bfile)
 ans=input("Do you wish to enter more records (y/n)? ")
 recno=recno+1
 if ans.lower()=='n':
    print("Record entry OVER ")
    print()
    break
# retrieving the size of file
print("Size of binary file (in bytes):",bfile.tell())
bfile.close()

# Reading the employee records from the file using load() module
import pickle
print("Now reading the employee records from the file")
print()
readrec=1
try:
    with open("empfile.dat","rb") as bfile:
        while True:
            edata=pickle.load(bfile)
            print("Record Number : ",readrec)
            print(edata)
            readrec=readrec+1
except EOFError:
   pass
#bfile.close()
