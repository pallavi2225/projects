#program for demonstarting decorators
def getval():
    return float(input("enter the value :"))

def square(kvr):
    def operation():
        n=kvr()
        res=n**2
        return n,res
    return operation

#Main program
op=square(getval)
n,Sqres=op()
print("square({})={}".format(n,Sqres))