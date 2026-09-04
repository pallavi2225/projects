
try:
    number =10/0

except ZeroDivisionError as e:
    print(e)
    print(type(e))


try:
    x=100/0
except Exception as e:
    print("Error:",e)


# print("else block will execute if there is no exception")
try:
    number=int(input("enter a number:"))
except ValueError:
    print("please enter a valid number")
else:
    print("you entered a valid number:", number)
    #When does else execute? Only when the try block completes successfully.


number=int(input("Enter a no:"))
try:
   result= 100 /number
except ZeroDivisionError:
    print("enter number greater than 0")
print(result)
