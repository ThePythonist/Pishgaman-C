def factorial(n):
    if n == 1 :
        return n
    else :
        return n * factorial(n-1)

n = int(input("Enter any number : "))

if n < 0 :
    print("Factorial does not exist")
elif n == 0 :
    print("Factorial of 0 is 1")
else :
    print("Factorial of",n,"is",factorial(n))
