#program for cal Div of Two Numbers

try:
    #taking the input from user
    num1=input("Enter the first value: ")
    num2=input("Enter the second value: ")
     
     #convrsio into intger
    s1=int(num1)
    s2=int(num2)
    result=s1/s2
except (ZeroDivisionError):
    print("You cannot enter zero")
except ValueError as kvr:
    print("kvr")
    #print("enter only numeric value")
else:
    print("-----else----")
    print("the first value is", s1)
    print("the result is",result)
    print("-----------")
finally:
    print("program execution is completed")


