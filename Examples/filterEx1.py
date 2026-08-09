def pos(val):
   if (val>0):
     return True
   else:
     return False
 

#Main Program
lst=[10,-20,30,0,-40,-50,60,70,-80,90,-100]
ps=filter(pos,lst)
print("type of ps",type(pos))
print("content of ps",ps)

#convert filter object into list object
pslst=list(ps)
print("given list:{}".format(lst))
print("Positivelist:{}".format(pslst))

