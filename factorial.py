""" Python program to find factoral
    using two method recursive and iterative"""

#By recursion method

def fact (n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


a=int(input("Enter the number to find the factorial: "))
print(f"The Factorial of {a} is {fact(a)}")

#By iteration method

def fact (n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

a=int(input("Enter the number to find the factorial: "))
print(f"The Factorial of {a} is {fact(a)}")
