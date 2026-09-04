numbers=[1,2,3,4]
squares={x: x* x for x in numbers }

print("dictionary with condition")
numb=[1,2,3,4,5,6]
even_squares={x: x * x  for x in numbers if x % 2 == 0}
print(even_squares)
#This is particularly useful when processing API/database data.