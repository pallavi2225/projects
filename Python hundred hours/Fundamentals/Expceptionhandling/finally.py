#finally executes whether an exception occurs or not.
try:
    number=10/2
    print(number)
except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("This always runs")