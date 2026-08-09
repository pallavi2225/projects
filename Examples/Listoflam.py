findmax= lambda values: max(values)
findmin= lambda values :min(values)


#main program
print("Enter list of values separatd by space:")
vals=[int(val) for val in input().split()]
print('Content of list=',vals)
bv=findmax(vals)
sv=findmin(vals)
print("Max({})={}".format(vals,bv))
print("Min({})={}".format(vals,sv))



