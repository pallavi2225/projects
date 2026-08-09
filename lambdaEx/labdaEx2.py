print("Enter the values separated by space : ")
lst=[int(val) for val in input().split()]

#main program
print("content of the list",lst)
poslist=list(filter(lambda val: val>0 and val%2==0,lst))
neglist=tuple(filter(lambda val: val<0 and val%2==0,lst))
print("positive even no={}".format(poslist))
print("negative even no={}".format(neglist))
