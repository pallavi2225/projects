marks = {
    "Python": 85,
    "SQL": 90,
    "Java": 75
}

print(min(marks))
print(max(marks))
print(sum(marks.values()))

print("tuple question")
numbers=(10,20,30,10,10)
print(numbers.count(10))
print(numbers.index(20))

print("list compreshension")

numbers = [i for i in range(1, 6)]
print(numbers)

squares = [i * i for i in range(1, 6)]