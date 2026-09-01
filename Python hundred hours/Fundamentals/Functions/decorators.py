# Decorators are functions that add extra behavior to another function.
def decorator_function(function):
    def wrapper():
        print("Before function")
        function()
        print("after function")
    return wrapper

def say_hello():
    print("hello")

say_hello= decorator_function(say_hello)
say_hello()

# def say_hi():
#     print("hi")

# say_hi = decorator_function(say_hi)
# say_hi()

