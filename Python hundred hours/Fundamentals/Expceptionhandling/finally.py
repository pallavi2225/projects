#finally executes whether an exception occurs or not.
# try:
#     number=10/2
#     print(number)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("This always runs")

try: 
    number=int(input("enter a number:"))
    result = 100 / number
except ValueError:
    print("please enter a valid input as Intereger")
except ZeroDivisionError:
    print("Number should be greater than zero")
else:
    print("Result is:", result)
finally:
    print("Program execution completed")

