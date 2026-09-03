#difference between sorted and sort()
#sorted() → returns a new sorted list
numbers=[2,6,7,8,9,3]
result=sorted(numbers)
print(sorted(numbers,reverse= True))
print(result)


#sort()  → modifies the original list
#sort() is a list method, while sorted() works with many iterables and returns a list.

nos=[7,8,9,1,2]
nos.sort()
print(nos)