#any() = Does at least one satisfy the condition? then true.
numbers=[1,3,5]
result=any(num % 2 == 0 for num in numbers)
print(result)

no=[2,4,1,3]
re=any(num % 2 ==0  for num in no)
print(re)


print("======All=====")
#all() Every condition must be True. 
no=[2,4,8,10]
result=all(nu % 2 == 0 for nu in no)
print(result)
# True output because all numbers are even.

numb=[1,3,4,5]
re=all(n % 2==0 for n in numb)
print(re)



