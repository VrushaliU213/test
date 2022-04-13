cube=lambda n1:n1**3
mul=lambda n1,n2:n1*n2
add=lambda n1,n2:n1+n2
sub=lambda n1,n2:n1-n2


def factorial(n):
    '''This is a function to find factorial
    of a number'''
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of a number",n,"is",fact)


















'''
def inputvalues():
    n1=int(input("Enter a number: "))
    n2=int(input("Enter a number: "))
    return n1,n2

ch=input("Enter your choice")

if(ch=="+"):
    n1,n2=inputvalues()
    print("Addition is",add(n1,n2))
elif(ch=="*"):
    n1,n2=inputvalues()
    print("Multiplication is",mul(n1,n2))
elif(ch=="!"):
    num=int(input("Enter a number:"))
    factorial(num)
else:
    print("Invalid choice")
    '''

