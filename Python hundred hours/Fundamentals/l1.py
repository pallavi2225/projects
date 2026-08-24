numbers=[50,10,40,30,20]

print("reverse")
# numbers.sort() Ascending order

print("reverse")
numbers.sort(reverse=True) #Descending order
print(numbers)


print("reverse")
a=[1,2,3,4,5]
a.reverse()
print(a)

fruits=["apple","banana","Mango"]
# for index, fruit in enumerate(fruits):
#     print(index,fruit)

for index, fruit in enumerate(fruits):
    print(index,fruit)

print("Custome index in enumerate")
brands=["Mochi","Gochi","Paragaon"]

for index, brands in enumerate(brands, start=1):
    print(index,brands)
    