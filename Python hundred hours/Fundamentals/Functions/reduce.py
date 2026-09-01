from functools import reduce
numbers=[1,2,3,4,5]
result=reduce(lambda a, b: a+b, numbers)
print(result)

#reduce() → one final result
nos=[10,30,56,78,45]
largest=reduce(lambda a,b: a if a > b else b,nos)
print(largest)


    