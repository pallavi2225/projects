#normal approch
numbers=[1,3,4,5]
squares=[]
for number  in numbers:
         squares.append(number * number)
print(squares)

#list comprehension approach
#"For every number in numbers, put number * number into the new list."
numbers=[1,3,4,5]
squares=[number * number for number in numbers]
print(squares)
#[expression for item in iterable if condition]

#only even numbers
even_numbers=[1,2,4,6,7,9]
even_numbers=[number for number in even_numbers if number % 2 == 0]
print(even_numbers)

#Squares of even numbers
even_no =[2,4,6,8]
result=[number * number for number in even_no if number % 2 ==0]
print(result)


