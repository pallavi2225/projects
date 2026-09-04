#Different problems can require different handling.
try:
    number = int(input("enter a number:"))
    result = 100/number
    print(result)
except ValueError:
    print("please enter a valid number")
    
except ZeroDivisionError:
    print("Number Cannot be zero")



   