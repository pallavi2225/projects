# age=-5
# if age < 0:
#     raise ValueError("Age cannot be negative")

# def register_user(age):
#     if age < 18:
#         raise ValueError("user must be 18 years or older")
#     print("Registrion successful")

# register_user(19)

try:
    number = int("10")
    result = 100 / number
except ValueError:
    print("Invalid")
else:
    print("Success:", result)
finally:
    print("Done")

try:
    number = int("abc")
    print("A")
except ValueError:
    print("B")
finally:
    print("C")