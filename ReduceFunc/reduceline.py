import functools
print("list of words separated  by comma:")
lst=[str(val) for val in input().split(",")]# ["Python","is","Invented", "by","Rossum"]
maxv=functools.reduce(lambda a,b:a+b,lst)
print("the longest word is:", maxv)
