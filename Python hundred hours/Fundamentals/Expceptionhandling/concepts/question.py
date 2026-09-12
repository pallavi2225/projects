def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient Balance")
    return balance-amount
try:
    new_balance=withdraw(5000,7000)
    print(new_balance)
except ValueError as e:
    print(e)


#     Function
#    ↓
# detects invalid situation
#    ↓
# raise Exception
#    ↓
# caller catches exception
#    ↓
# handles it

# ValueError
# TypeError
# IndexError
# KeyError
# ZeroDivisionError
# FileNotFoundError