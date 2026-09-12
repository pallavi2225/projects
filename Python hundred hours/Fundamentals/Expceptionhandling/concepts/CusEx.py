# age=-5
# if age < 0:
#     raise ValueError("Age cannot be negative")

def register_user(age):
    if age < 18:
        raise ValueError("user must be 18 years or older")
    print("Registrion successful")

register_user(19)