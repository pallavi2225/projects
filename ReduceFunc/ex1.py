import functools as fc

print("Enter values separeted by space:")

lst=[float(val) for val in input().split()]
res=fc.reduce(lambda k,v: k+v,lst)
print("sum=",res)

