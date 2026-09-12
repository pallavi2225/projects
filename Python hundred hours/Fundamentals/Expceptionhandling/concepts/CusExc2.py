def check_age(age):
    if age < 18:
        raise ValueError("user must be 18+")
    print("Registraction Successful")
try:
    check_age(20)
except ValueError as e:
    print("Registraion failed",e)