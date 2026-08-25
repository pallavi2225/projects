print(10+20)
name="Pallavi"
age=30
salary=40000
new_Salary=salary+10000
print(new_Salary)
print(type(age))
print(type(name))
isworking= True
print(type(isworking))
print(isworking)
a=10
b=3
c=a+b
print(c)
d=a-b
print(d)
e=a*b
print(e)
f=a/b
print(f)
g=a//b
print(g)
h=a%b
print(h)
print("************")
p=10
q=20
result=p==q
print(result)
print(p!=q)
print(p>q)
print(p<q)
print(p>=q)
print(p<=q)
print(10>5)
# name=str(input("Enter your name:"))
# print(name + "Thorat")
# age=int(input("Enter your age:"))
# print(age + 2)

print("******* Simple Salary Calculator *******")
EmployeeName= str(input("Enter Employee Name:"))
EmployeeSalary=float(input("Enter Employee Salary:"))

Bonus=EmployeeSalary * 0.15
Transport=2000
New_Salary=EmployeeSalary+ Bonus + Transport 
print("**********Details of New Employee **********")
print("Employee Name:", EmployeeName)
print("Employee Salary:", EmployeeSalary)
print("New Salary:", New_Salary)    
print("************end of program*******************")
