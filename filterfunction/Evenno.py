#list of numbers
numbers=[1,2,3,4,5,6,7,8]

#function to check the even no
def is_even(num):
    return num % 2==0

#function call
#filter() keeps only values where fucntion returns true
even_numbers=list(filter(is_even, numbers))

print("even Nmbers:", even_numbers)
