Student={
    "Name" : "Pallavi",
    "age" : 34,
    "city" : "Mumbai"
}
# print(Student.get("Name"))
# print(Student.keys())
# print(Student.values()
# print(Student.items())

# for key, value in Student.items():
#     print(key, value)

# Student.update({
#     
# })

Student.update({
    "Location": "Banglore",
    "post": "Python Developer",
    "Salary": 50000
})

for key, value in Student.items():
    print(key,value)
print(Student)

Student2=Student.copy()

person={
    "name":"Manoj"
}
person.setdefault("age",34)

print(person)

print("------")
keys = ["name", "age", "city"]
# Student=Student2.fromkeys(key)
# Student=dict.fromkeys(keys,"Not Available")
print(Student)

print("-------For loop in dictionary-----")
print("print keys")
for key in Student:
    print(key)

print("-----------printValues-----------")
for value in Student.values():
    print(value)

print("----------print items----------")
for key, value in Student.items():
    print(key,":", value)



