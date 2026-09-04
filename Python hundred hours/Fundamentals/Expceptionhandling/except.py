try:
    print("A")
    result=10/0   #ZeroDivisionError: division by zero
    print("B")
except:
    print("c")

print("D")
#executing the remaining statements in that try block and jumps to the matching except.

print("Q1")
try:
    number=int("hello")
except ValueError:
    print("Please enter a valid number") 
    #Because ValueError tells us exactly what we're handling.So, it's a good practice to use specific exceptions rather than a general except statement.

print("Q2")
try:
    text=input(str("Enter a name:"))
except ValueError:
    print("please enter aa valid string")
