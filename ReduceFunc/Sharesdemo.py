import shares,time
import importlib

#import time


def dispshares(d):
    print("----------------------------")
    print("ShareName\t\t shareValue")
    print("----------------------------")
    for sn,sv in d.items():
        print("\t{}\t\t{}".format(sn,sv))
        print("----------------------------")

#Main Program
d= shares.shareInfo()#functioncall
dispshares(d)
#======
print("Waiting for 10 seconds to get the updated share values")
time.sleep(20)  
print("Getting the updated share values")
#====
#Reloading the module to get the updated share values
importlib.reload(shares)
d=shares.shareInfo()
dispshares(d)









