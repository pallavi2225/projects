try:
    s1=input("Enter the first value: ")
    s2=input("Enter the second value:")
    n1=int(s1)
    n2=int(s2)
    result=n1/n2
except ValueError:
    print("please enter a valid value")
except ZeroDivisionError:
    print("Division by 0 is not allowed")
except IndexError:
    print("index error occured")
except  Exception as e:
    print("Something went wrong", e)
else:
    print("-----else-----")
    print("the first value is", n1)
    print("the second value is , n2")
    print("the result is", result)
    print("-------------")
finally:
    print("program terminated")

    
