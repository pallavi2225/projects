#**kwargs - Accepts Multiple keyword arguments -(internaly)Dictionary

#When defining a function, the usual parameter order is:
# def function(
#     normal_parameters,
#     *args,
#     keyword_only_parameters,
#     **kwargs
# )
#Positional arguments → *args → **kwargs

def example(*args,**kwargs):
    print(args)
    print(kwargs)
example(
    10,
    20,
    name="Pallavi",
    city="Mumbai"
)

def employee(**kwargs):
    for key , value in kwargs.items():
        print(key,":",value)
employee(
    name="Rani",
    age=32,
    city="Mumbai"
)

print("Access a Specific Value == Because kwargs is a dictionary:")
def emp(**kwargs):
    # print(kwargs["name"])
    print(kwargs.get("name"))
emp(
    name="Dhriti",
    age=23
)

print("Excercise Q")
def student(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
student(
    name="Pallavi",
    age=34,
    course="Python"
)