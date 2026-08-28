#Scope means where a variable can be accessed in your program. 1 global ,2local

def greet():
    message="Hello"    #local variable
    print(message)
greet()

message="come"   #global varibale
def come():
    print(message)
come()

name="Pallavi"
def test():
    age=34
    print(name)
    print(age)
test()
print(name)
#print(age)# error bcoz local variable

#name → accessible globally
#age → accessible only inside test()

# count=10
# def increase():
#     global count  #To modify the global variable, we can use: global keyword
#     count=count+1
#     print(count)
# increase()
# print(count)

print("cleaner and safer")
# def inc(count):
#     return count+1
# count=10
# count=inc(count)
# print(count)

print("Excersice")
def test():
    number=10
    print(number)
test()
 
count=5
def increase():
    global count
    count=count+1
    print(count)
increase()
print(count)