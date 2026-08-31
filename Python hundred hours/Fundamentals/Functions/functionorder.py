#the common order
def example(
        normal,
        default="value",
        *args,
        keyword_only,
        **kwargs
   ):
    pass

def employee(name,age=30,*skills, city="Mumbai",**details):
    print(name)
    print(age)
    print(skills)
    print(city)
    print(details)
