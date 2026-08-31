# Type hints don't automatically force Python to reject incorrect types at runtime in normal Python.
# But they help:
# VS Code
# Linters
# Type checkers
# Developers reading your code

def add(a,b):
    return a+b
# a → expected int
# b → expected int
# return → expected int

def greet(name:str)-> str:
    return f"Hello {name}"