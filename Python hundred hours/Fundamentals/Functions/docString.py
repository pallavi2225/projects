def add(a,b):
    """ Returns the sum of two numbers"""  #The text inside triple quotes is documentation.
    return a + b


#access it

print(add.__doc__)

def calculate_total(pricess):
    """Calculate and returns the total price"""
    return sum(pricess)
# calculate_total()