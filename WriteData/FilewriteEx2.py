srno=int(input("Enter No  :" ))
sname=str(input("Enter Name : "))
smarks=float(input("Enter marks:"))

with open("Schoolstudent.data","a") as fp:
    fp.write(str(srno)+ "\n")
    fp.write(sname + "\n")
    fp.write(str(smarks)+"\n")
    print("Data written to the file")

