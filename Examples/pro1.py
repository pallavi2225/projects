# print("Hello world")
# print("I Am python ")
# #Addition of two numbers
# def addop(a,b):
#     print("I am in function Def")
#     c=a+b
#     return c
#     res=addop(100,200)
#     print(res)

#calculate simple intrest
def simpleint():
    p=float(input("enter the Principal amount :"))
    t=float(input("Enter the time : "))
    r=float(input("enter rate of intrest : "))
#caculate si ant total amt to pay
    si=(p*t*r)/100
    totalamt=p+si
    print(totalamt,si)
simpleint()
