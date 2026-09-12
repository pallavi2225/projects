# Custom exceptions allow us to represent application-specific or 
# business-specific errors clearly and 
# handle them separately from generic Python errors.

class InsuffcientBalanceError(Exception):
     pass
try:  
    balance=500
    withdraw_amount=7000

    if withdraw_amount > balance:
     raise InsuffcientBalanceError("InsuffcientBalance")

except InsuffcientBalanceError as e:
   print(e)