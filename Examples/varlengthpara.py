#Program to generate variable length Argument or Parameter.
#in the positional parameter default parameter should be written at the end, after the variable length parameter.
def info(Srno,Sname,*a):
    print("Student No=",Srno)
    print("StudentName",Sname)
    print(a,type(a))
 


info(100,"Rs",10,20,30,40,50)
print("----------")
info(200,"Vk",10,20,30,40)
print("----------")
info(300,"RT",10,20,30)
print("----------")
info(400,"VP",10,20)
print("----------")
info(500,"ST",10)