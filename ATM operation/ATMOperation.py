from ATMExcept import DepositError, WithdrawError, InSuffundError
bal=500.00

def deposite():
     damt=float(input("Enter ur Deposite Amount:"))
     #Implicity valueError Raises when value is alnum or symbols or piure str
     if(damt<=0):
                raise DepositError
     else:
             global bal
             bal=bal+damt
             print("Ur Account xxxxxxxx123 Credited with INR:{}".format(damt))
             print("Now Ur Account xxxxxxxx123 Bal INR:{}".format(bal))

def withdraw():
        wamt=float(input("Enter Ur withdraw Amount:"))
        #Implicity ValueError Raises when value is alnum or symbols or pure str
        global bal
        if(wamt<=0):
                raise WithdrawError
        elif((wamt+500)>bal):              #min bal 500 condition
                raise InSuffundError     
        else:
                bal=bal-wamt
                print("ur Account xxxxxxxx123 Debitted with INR:{}".format(wamt))
                print("Now Ur Account xxxxxxxx123 bal INR:{}".format(bal))

def balenq():
        print("ur Account xxxxxxxx123 Bal INR:{}.format(bal)")
                  


          