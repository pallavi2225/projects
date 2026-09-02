def calculators(a,b):
    return a+b,a-b
addition,subtraction=calculators(12,23)

print(addition)
print(subtraction)

def cal(a,b):
    addition =a+b
    multiplication= a*b
    return addition, multiplication

result=print(cal(10,20))



#Function returning Dictionary
def create_user(name,age):
    return{
        "name":name,
        "age":age
    }

user =create_user("Pallavi",34)
print(user)


#validation
def divide(a,b):
    if b==0:
        return "cannot divide by zero"
    
    return a/b

        
