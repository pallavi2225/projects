
# *args allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple.

def add(*args):
    total=0
    for number in args:
        total = total + number
    return total
print(add(12+34))