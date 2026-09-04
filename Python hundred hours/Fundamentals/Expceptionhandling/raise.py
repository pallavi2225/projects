try:
    age=-5
    if age > 0 :
       raise ValueError("Age should be greater than zero" )
except ValueError as e:
    print("error:", e)


try:
    def withdraw(balance,amount):
        if amount > balance:
           raise ValueError("insufficient Balance")
           print(balance-amount)
except ValueError as e:
    print("error:",e)
    
withdraw(500,1500)