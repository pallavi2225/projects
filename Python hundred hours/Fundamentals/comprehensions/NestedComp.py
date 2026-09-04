# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result=[]
# for row in matrix:
#     for number in row:
#         result.append(number)
# result=[number for  row in matrix for number in row]
# print(result)

matrix=[
    [11,12,13],
    [14,15,16],
    [17,18,19]
]
result=[]

for row in matrix:
    for number in row:
        result.append(number)
        result=[number for row in matrix for number in row]
        print(result)

print("Nested Comprehension")

matrix=[
    [1,2],
    [3,4],
    [5,6]
]

result=[number * 10
        for  row in matrix
         for number in row
           ]

#equivalent code

result=[]
for  row in matrix:
        for  number in  row:
         result.append(number * 10)
print(result)

print("Nested comprehension with condition")
matrix=[
     [1,2,3],
     [4,5,6],
     [7,8,9]
]
result=[
     number 
     for row in matrix
     for number in row
     if  number % 2 ==0
]
print(result)
