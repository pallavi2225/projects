#program for keyword arguments
def stdinfo(Srno,dep,age,city,state):
    print("\t{}\t{}\t{}\t{}\t{}".format(Srno,dep,age,city,state))

#main program
print("\tSrno\tdep\tage\tcity\tstate")
#stdinfo(1,"comsci",23,"banglore","maharashtra")
stdinfo(dep="Arts",Srno=1,city="hydrabad",age=23,state="Gujrat")
