try:
    number= 10/0
except :
    print("Something went wrong")
print("program completed")

try:
    print("A")
    print(10/0)
    print("B")
except:
    print("c")
print("D")

try:
    result=10/0
except ZeroDivisionError:
    print("You cannot didvide by zero")

try:
    age= int("hello")
except ValueError:
     print("please enter a valid  number")

try:
    age=int(input("Enter  your age: "))
    print("your age is :", age)

except ValueError:
    print("please enter a  valid number.")

try:
    number =int(input("enter number:"))
    result = 100/ number
    print(result)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("number cannot be zero")

try:
    number=int(input("Enter a number"))
except ValueError:
    print("invalid number")

try:
    result=10/0
except Exception as e:
    print(e)
    print(type(e))