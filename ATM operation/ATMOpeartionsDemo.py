from ATMMenu import Menu 
from ATMOperation import deposit,withdraw,balenq
from ATMExcept import DepositError,WithdrawError,InSuffundError
while(True):
    try:

        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
                  case 1:
                     try:
                          deposit()
                     except ValueError:
                          print("\tDont enter alnums,strs,symbols for Depositing the amt:")
                     except DepositError:
                          print("\tDont try to depositr -Ve Amount Or Zero in the account")

                   case 2:
                      try:
                         withdraw()
                    except ValueError:
                        print("\tDont enter alnums,strs,symbols for withdraw the amount:")
                    except WithdrawError:
                         print("\tDont try to withdraw -Ve Amount Or 0 from the account")
                    except InSuffundError:
                          print("\t Ur Account does not have Suff funds---")
        
                   case 3:
                        balenq()
                  case 4:
                       print("Thn for Unsinh Program")
                       break
                 case_:
                         print("Ur Selection of operation is wrong --try again")
        

 except ValueError:
             print("Dont Enter alnums,strs and symbols for choice --try again")       
        
        


        



                         
