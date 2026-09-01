from functools import reduce
#Q1
numbers=[2,3,4,5]
multiply = reduce(lambda a,b:a*b, numbers)
print(multiply)