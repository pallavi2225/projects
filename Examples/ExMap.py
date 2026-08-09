def increment(sal):
    sal=sal+sal*(20/100)
    return sal

print("Enter list of old Salaries:")
oldsals=[float(sal) for sal in input().split()]
print("list of old Salaries :",oldsals)



#convert map object into list
newsal=list(nsl)
print("New Sal list=",newsal)