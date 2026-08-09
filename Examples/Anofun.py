palindrome=lambda x: "Palindrome" if str(x)==str(x)[::-1] else "Not Palindrome"

#main program
n=input("Enter a no / value:")
res=palindrome(n)
print("{} is {}".format(n,res))