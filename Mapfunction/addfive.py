numbers=[10,20,30,40,50]

def add_five(x):
    return x+5

result=list(map(add_five, numbers))
print(result)
