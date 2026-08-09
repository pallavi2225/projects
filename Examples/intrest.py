#program to pay intrest
#function Chaining
def takevalues():
   p=float(input("enter an Amount : "))
   r=float(input("enter  rate of intrest : "))
   t=float(input("enter the time : "))
   return p,t,r

def calsimpleintrest():
   p,t,r=takevalues()
   si=(p*t*r)/100
   totalamount=p+si
   return p,t,r,si,totalamount

def displayresult():
   p,t,r,si,totalamount=calsimpleintrest()
   print("Principal Amount :{}".format(p))
   print("time :{}".format(t))
   print("rate of intrest:{}".format(r))
   print("simple intrest:{}".format(si))
   print("total amount:{}".format(totalamount))

#Main program
displayresult()
     
   

