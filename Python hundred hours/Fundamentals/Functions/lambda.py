def add(a,b):
    return a+b

#using lambda
#A lambda function is a small, anonymous function.
#lambda arguments: expression


add =lambda a,b: a+b
print(add(4,8))

#Normal function
def square(a):
    return a*a
print(square(4))

#lambda function
square= lambda a: a* a
print(square(5))

multiply= lambda a ,b: a * b
print(multiply(3,9))

#lambda with condition 
check = lambda  a: "even" if a % 2 ==0 else "odd"
print(check(10))

#lambda with map
nos=[1,2,3,4,5]
squares=list(map(lambda no: no * no,nos))
print(squares)

numbers=[1,2,3,4,5]
multiplybytwo=list(map(lambda no: no * 2,numbers))
print(multiplybytwo)


#map(function, iterable)
num=[1,2,3,4,5]
mulbythree=list(map(lambda no: no*3,num))
print(mulbythree)


#filter() selects items based on a condition.
#filter(condition_function, iterable)
series=[1,2,3,4,5,6]
squ=list(filter(lambda n:n % 2 ==0,series))
print(squ)

# filter even no only
numbers=[10,15,20,25,30]
even_numbers=list(filter(lambda number: number % 2 ==0,numbers))
print(even_numbers)