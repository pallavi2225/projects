
# *args allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple.
#*args -Accepts Multiple positional arguments -(internally)Tuple


def introduce(name, *skills):
    print("Name:",name)
    print("Skills:",skills)
introduce(
    "Pallavi",
    "Python",
    "Sql",
    "FastApi"
)

def add(*args):
    total=0
    for number in args:
        total = total + number
    return total
print(add(12+34+40+55))


print("Excercise")
def total(*numbers):
    return sum(numbers)
result=(total(2,3,4,5))
print(result)

def show_name(*names):
 for name in names:
    print(name)
show_name("Rahul","Pallavi","Sneha")

# res=show_name("Rani","Ritu","Manoj","Pallavi")
# print(res)
              