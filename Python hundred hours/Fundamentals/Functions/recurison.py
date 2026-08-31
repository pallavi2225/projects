# Recursion means a function calls itself.
def countdownone(number):
    print(number)
    if number > 0:
        countdownone(number-1)
countdownone(6)


def countdown(number):
    #Base case
    if number ==0:
        print("finished")
        return
    
    #Recursive case
    print(number)
    countdown(number-1)
countdown(7)

#example factorial
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)

print(factorial(5))