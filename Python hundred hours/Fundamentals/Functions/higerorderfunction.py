# A higher-order function is a function that:
# Accepts another function as an argument, or
# Returns another function.

def apply_operation(function, number):
    return function(number)

def square(number):
    return number * number
# print(square(5))
print(apply_operation(square,5))

# Because we're passing the function itself, not calling it immediately.
# This is important for callbacks and frameworks.