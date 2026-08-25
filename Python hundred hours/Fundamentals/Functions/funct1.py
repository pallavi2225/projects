def greet(name):
    print("Hello ", name)
greet("Pallavi")

def introduced(name, age):
    print("My name is", name)
    print("My age is ", age)
introduced("Rani", 23)

print("Default parameter")
def greets(name="Sir"):
    print("Hello",name)
greets()

#Parameters without default values should come before parameters with default values.
def intro(name, city="Mumbai"):
    print(name)
    print(city)
intro("Revati")

def divide(a,b):
    return a/b
print(divide(2,10))


#With keyword arguments, you explicitly mention the parameter name.
def introduce(name, age ,city):
    print(name)
    print(age)
    print(city)

introduce(
    city="Mumbai",
    name="Pallavi",
    age=23
)

print("function excercise")

print("Q1")
def country(name="India"):
    print(name)
country()


print("Q2")
def employee(name,age,city):
   return name,age,city
result =employee(
    name="Pallavi",
    age=34,
    city="Mumbai"
)
print(result)

print("Q3")
def multiply(a,b):
    return a * b
resultt=multiply(5,10)
print(resultt)


