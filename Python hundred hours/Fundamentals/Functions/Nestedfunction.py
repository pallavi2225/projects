
def outer(name):
    
    def inner():
        print("hello",name)
    return inner()

greet =  outer("Pallavi")
# print(greet)
