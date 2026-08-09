tkt=input("Do you have Ticket(yes/No):")

if(tkt=="No"):
    print("please buy the ticket to watch the movie")

if(tkt=="yes"):
    age=int(input("Enter Your age:"))
    if(age>=18):
        print("You can watch the movie")
    if(age<18):
        print("you cannot watch the movie")


    
    
    