#Program for demonstrating writing the data to the file
#FileWriteEx1.py
sno=101
sname="Travis"
marks=56.99
print(sno,sname,marks)

with open("Student.txt","w") as f:
   # f.write(f"{sno}{sname}{marks}")

    #wite data in separate line
    f.write(str(sno)+ "\n")
    f.write(str(sname + "\n"))
    f.write(str(marks)+ "\n")
    print("Data written to the file")

