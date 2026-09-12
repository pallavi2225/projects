try:
    number=int("10")
except ValueError:
    print("invalid number")
else:
    print("successful conversion")

try:
    print(10/10)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("this is always executes")

#finally id useful for resources
# file=open("data.txt")
# try:
#     data=file.read()
# finally:
#     file.close()

try:
    number=int(input("Enter the number"))
    result=100/number
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result", result)
finally:
    print("program finished")