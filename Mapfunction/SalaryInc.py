def increment(sal):
    sal= sal + sal * (20/100)
    return sal 

print("Enter list of old salaries:")
oldsals=[float(sal) for  sal in input().split()]
print("List of old Salaries:",oldsals)
nsl=map(increment, oldsals)

#convert map object into list
print(type(nsl))
newsal=list(nsl)
print("list of new salaries:", newsal)
z=zip(oldsals,newsal)
print(z)