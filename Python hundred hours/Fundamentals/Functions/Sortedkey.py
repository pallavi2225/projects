#Suppose we want to sort students based on their marks. we use key.
students=[
    ("Pallavi",85),
    ("Manoj",67),
    ("Sneha",78)
]
result=sorted(students, key=lambda student:student[1])
print(result)

employees=[
    {"name":"Pallavi","salary":50000},
    {"name": "Manoj","salary": 60000},
    {"name": "Amrita","salary":40000}
]
result=sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True 
)
#for descending oredr we use reverse = True
